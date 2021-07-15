class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1: return 0
        
        cost = 0
        size = len(arr)
        visited = [False] * size
        visited[0] = True
        
        same = collections.defaultdict(list)
        for p, n in enumerate(arr):
            same[n].append(p)
            
        st = [0] # contains same cost vals
        cost = 0
        
        while True:
            nxt = []
            cost += 1
            # print(st)
            while st:
                cur = st.pop()
                # print()
                for nei in same[arr[cur]] + [cur-1, cur+1]:
                    # print(nei, end=' ')
                    if nei == cur or not 0 <= nei < size:
                        continue
                    if nei == size - 1:
                        # print(st)
                        return cost
                    if not visited[nei]:
                        visited[nei] = True
                        nxt.append(nei)
            st = nxt
            
            
        
        

