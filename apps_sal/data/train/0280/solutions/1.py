class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        visited = {}
        dic = {}
        def dfs(start, k):
            if (start, k) in dic:
                return dic[(start,k)]
            if k == 0:
                i = start
                j = n-1
                dic[(start, k)] = visited[(i,j)]
                return visited[(i,j)]
            count = float('inf')
            for i in range(start+1, n-k+1):
                count = min(count, visited[(start, i-1)]+dfs(i, k-1))
            
            dic[(start, k)] = count
            #print(dic)
            return count
        for j in range(n):
            for i in range(j, -1, -1):
                if i == j:
                    visited[(i,j)] = 0
                elif i == j-1:
                    if s[i] != s[j]:
                        visited[(i,j)] = 1
                    else:
                        visited[(i,j)] = 0
                else:
                    if s[i] == s[j]:
                        visited[(i,j)] = visited[(i+1,j-1)]
                    else:
                        visited[(i,j)] = visited[(i+1,j-1)]+1
        
        return dfs(0, k-1)

