class Solution:
    def lenLongestFibSubseq(self, array: List[int]) -> int:
        if len(array)<3:
            return len(array)
        d={}
        ans=0
        dp=[[2 for i in range(len(array))] for j in range(len(array))]
        for i in range(len(array)):
            d[array[i]]=i
        for i in range(len(array)-1):
            for j in range(i+1,len(array)):
                if array[i]+array[j] in d:
                    dp[j][d[array[i]+array[j]]]=1+dp[i][j]
                    if dp[j][d[array[i]+array[j]]]>ans:
                        ans=dp[j][d[array[i]+array[j]]]
        return ans

