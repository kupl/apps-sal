from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        if n < K:
            return 0

        # 3 pointer sliding window
        # p1 points to the 1st unique integer, start of the window
        # p2 points to the first occurrance of the Kth unique integer after p1
        # p3 points the the first occurrance of the next unique integer after p2, of end of string at n
        # Given such a window, we add (p3-p2) to the count
        # Then move p1 by 1. Check if that reduces the number of integers to K-1. If no, add p3-p2 again.
        # If yes, then move p2 until the count goes up to K again. If p2 lands on p3 when doing this,
        # then need to move p3 to the next integer. If p3 is already at EOS, return

        # To maintain the number of unique integers in a window, we'll use a hashmap
        # Be careful, we need this dict to contain only nonzero count entries. So if a count becomes zero, delete it!
        count = defaultdict(int)
        p1 = 0
        p2 = 0
        p3 = 0
        count[A[0]] += 1
        ans = 0
        while p2 < n:  # IMPORTANT: Use p2 rather than p3, because we want to execute as long as p2 can expand, even if p3 is already at n
            # Move p2 until the number of unique integers in the window hits K
            remaining = K - len(count)
            while remaining > 0:
                p2 += 1
                if p2 == n:
                    return ans
                count[A[p2]] += 1
                if count[A[p2]] == 1:
                    remaining -= 1
            # p2 now points to the first instance of the Kth integer after p1
            # Now move p3 to the next unique integer after p2
            # print(\"count: {}, A[{}]: {}, {}\".format(count, p3, A[p3], A[p3] in count))
            while p3 < n and A[p3] in count:
                p3 += 1
            # p3 is either n or points to the (K+1)th integer after p1
            # Now, keep adding (p3-p2) to the count and advancing p1 until we no longer have K integers in this window
            while len(count) == K:
                ans += (p3 - p2)
                # print(\"p1:{}, p2:{}, p3:{}, count:{}\".format(p1, p2, p3, count))
                p1 += 1
                count[A[p1 - 1]] -= 1
                if count[A[p1 - 1]] == 0:
                    del count[A[p1 - 1]]
        return ans
