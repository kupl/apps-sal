class Solution:
    def minJumps(self, arr: List[int]) -> int:
        def BFS(queue):
            seen = [1]*len(arr);seen[0] = 0
            while queue:
                var , level = queue.pop(0)
                if var == len(arr) - 1:return level
                if seen[var + 1]:queue.append([var+1,level+1]);seen[var+1] = 0
                if var - 1 >=0 and   seen[var - 1]:queue.append([var-1,level+1]);seen[var-1] = 0                 
                for i in d[arr[var]]:
                    if seen[i]:queue.append([i,level+1]);seen[i] = 0
                d[arr[var]].clear()
        
        d = defaultdict(list)
        for i in range(len(arr) - 1 , -1 ,-1 ):d[arr[i]] +=[i]
        return (BFS([[0,0]]))
