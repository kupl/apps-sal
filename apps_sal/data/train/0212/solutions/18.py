class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        # Time  complexity: O(N^2)
        # Space complexity: O(N)
        # A.sort()
        # dic = {num: 1 for num in A}
        # for i in range(1, len(A)):
        #     for j in range(i):
        #         q, res = divmod(A[i], A[j])
        #         if res == 0 and q in dic:
        #             dic[A[i]] += dic[q] * dic[A[j]]

        # return sum(dic.values()) % (10**9 + 7)

        dp = {}
        for a in sorted(A):
            dp[a] = sum(dp[b] * dp.get(a // b, 0) for b in dp if a % b == 0) + 1
        return sum(dp.values()) % (10**9 + 7)
