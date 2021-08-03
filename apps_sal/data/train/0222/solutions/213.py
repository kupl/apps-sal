class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        # 1. Brutal Force
        # l = ans = 0
        # mapA = set(a)
        # for i in range(len(A)):
        #     for j in range(i+1, len(A)):
        #         x, y = A[j], A[i] + A[j]
        #         l = 2
        #         while y in mapA:
        #             x, y = y, x + y
        #             l += 1
        #         ans = max(ans, l)
        # return ans if ans >= 3 else 0

        # 2. DP
        from collections import defaultdict
        ans = 0
        mapA = {n: i for i, n in enumerate(A)}
        dp = defaultdict(lambda: 2)
        for k, z in enumerate(A):
            for j in range(k):
                i = mapA.get(z - A[j])
                if i is not None and i < j:
                    temp = dp[(j, k)] = dp[(i, j)] + 1
                    ans = max(ans, temp)
        return ans if ans >= 3 else 0
