class Solution:
    def countVowelPermutation(self, n: int) -> int:
        result = [1]*5
        graph = [[1],[0,2],[0,1,3,4],[2,4],[0]]
        for count in range(1,n):
            tempResult = [0]*5
            for i in range(5):
                for j in graph[i]:
                    tempResult[j]+=result[i]
            result = tempResult
        return sum(result)%(10**9+7)
