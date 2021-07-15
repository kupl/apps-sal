class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        '''
        n = len(arr)
        parents = list(range(n))
        ranks = [0] * n
        groupCounts = [0] * (n+1)
        counts = [1] * n
        visited = [False] * n
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            
            return parents[x]
    
        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            
            if r1 != r2:
                groupCounts[counts[r1]] -= 1
                groupCounts[counts[r2]] -= 1
                counts[r1] = counts[r2] = counts[r1] + counts[r2]
                groupCounts[counts[r1]] += 1
                
                if ranks[r1] >= ranks[r2]:
                    parents[r2] = r1
                    ranks[r1] += 1
                else:
                    parents[r1] = r2
                    ranks[r2] += 1
        
        last = -1
        
        for step, index in enumerate(arr):
            index -= 1
            groupCounts[1] += 1
            if index-1 >= 0 and visited[index-1]:
                union(index, index-1)
            
            if index+1 < n and visited[index+1]:
                union(index, index+1)
            
            visited[index] = True
            
            if groupCounts[m]:
                last = step + 1

        return last
        '''
        n = len(arr)
        length = [0] * (n+2)
        count = [0] * (n+1)
        ans = -1
        
        for step, index in enumerate(arr):
            left = length[index-1]
            right = length[index+1]
            length[index-left] = length[index+right] = left + right + 1
            count[left] -= 1
            count[right] -= 1
            count[length[index-left]] += 1
            
            if count[m]:
                ans = step + 1
        
        return ans
