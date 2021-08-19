from collections import defaultdict


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        if n < K:
            return 0
        count = defaultdict(int)
        p1 = 0
        p2 = 0
        p3 = 0
        count[A[0]] += 1
        ans = 0
        while p2 < n:
            remaining = K - len(count)
            while remaining > 0:
                p2 += 1
                if p2 == n:
                    return ans
                count[A[p2]] += 1
                if count[A[p2]] == 1:
                    remaining -= 1
            while p3 < n and A[p3] in count:
                p3 += 1
            while len(count) == K:
                ans += p3 - p2
                p1 += 1
                count[A[p1 - 1]] -= 1
                if count[A[p1 - 1]] == 0:
                    del count[A[p1 - 1]]
        return ans
