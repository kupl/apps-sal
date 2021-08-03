'''
9 4 7 2 10

抽两个数 得到等差 计算所有的组合
dp[(j, dif)]指的是以dif为等差， 截至（包含）A[j], 的最长等差序列
'''


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dif = A[j] - A[i]
                dp[(j, dif)] = dp.get((i, dif), 1) + 1
        return max(dp.values())
