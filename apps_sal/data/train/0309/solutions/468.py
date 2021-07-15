class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        #这题bottom up写起来快?
        dp = defaultdict(lambda: 1) #default 是 1， 自己肯定是自己的seq
        for i in range(len(A)):
            for j in range(i): #之前的
                diff = A[i] - A[j]
                dp[(i, diff)] = max(dp[(i, diff)], 1+ dp[(j, diff)])
                
        return max(dp.values())
