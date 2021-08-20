class Solution:

    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        sorted_A = sorted(A)
        dp = dict()
        result = 0
        for i in range(len(sorted_A)):
            cur_total = 0
            for j in range(i + 1):
                cur_val = sorted_A[i]
                prev_val = sorted_A[j]
                if i == j:
                    dp[cur_val] = cur_total + 1
                    result += cur_total + 1
                elif cur_val / prev_val in dp:
                    cur_total += dp[cur_val / prev_val] * dp[prev_val]
        return result % (10 ** 9 + 7)
        '\n        \n        \n        [18, 3, 6, 2]\n        [2, 3, 6, 18]\n        dp = {\n            2 : 1\n            3 : 1\n            6 : 3\n            18: 5\n        }\n        cur_val = 18\n        prev_val = 6\n        cur_total = 3 + 1 \n        result = 1 + 1 + 3 + 5\n        \n        \n        '
