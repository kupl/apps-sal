class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        parents = list(range(n))
        ranks = [0] * n
        counts = [1] * n
        groupCounts = [0] * (n+1)
        cur_string = [0] * n
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            
            return parents[x]
        
        def union(x,y):
            r1 = find(x)
            r2 = find(y)
            
            groupCounts[counts[r1]] -= 1
            groupCounts[counts[r2]] -= 1
            counts[r1] = counts[r2] = counts[r1] + counts[r2]
            groupCounts[counts[r1]] += 1
            
            if r1 != r2:
                if ranks[r1] >= ranks[r2]:
                    parents[r2] = r1
                    ranks[r1] += 1
                else:
                    parents[r1] = r2
                    ranks[r2] += 1
        
        ans = -1
        
        for step, i in enumerate(arr):
            i -= 1
            groupCounts[1] += 1
            
            if i - 1 >= 0 and cur_string[i-1] == 1:
                union(i, i-1)
            
            if i + 1 < n and cur_string[i+1] == 1:
                union(i, i+1)
            
            cur_string[i] = 1
            
            if groupCounts[m]:
                ans = step + 1
        
        return ans

