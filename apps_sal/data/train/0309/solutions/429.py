# dict.get(key,number) return number if get None
# 用dict 紀錄 dict[(id,diff)]: count
# dict[(new id,diff)] = dict[(old id,diff)] || 1 + 1
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                x = dp.get((i, A[j] - A[i]), 1)
                # print(x)
                dp[j, A[j] - A[i]] = x + 1
            # print(dp)
        return max(dp.values())
