from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if K == 0:
            return 0
        res1 = self.helper(A, K)
        res2 = self.helper(A, K - 1)

        return res1 - res2

    def helper(self, a, k):

        if k == 0:
            return 0

        count = defaultdict(int)

        result = 0
        l = 0
        r = 0

        while r < len(a):
            count[a[r]] += 1

            while len(count) > k:
                count[a[l]] -= 1
                if count[a[l]] == 0:
                    count.pop(a[l])
                l += 1

            result += r - l + 1
            r += 1

        return result

