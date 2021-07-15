class Solution:
    def minJumps(self, arr: List[int]) -> int:
        L = len(arr)
        if L<2:
            return 0
        cnt = defaultdict(list)
        for i,val in enumerate(arr):
            cnt[val].append(i)
            
        q = deque([0])
        visited = {0}
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                n = q.popleft()
                if n==L-1:
                    return steps
                for el in cnt[arr[n]]:
                    if el not in visited:
                        q.append(el)
                        visited.add(el)
                cnt[arr[n]].clear()
                for c in [n-1,n+1]:
                    if 0<=c<L and c not in visited:
                        q.append(c)
                        visited.add(c)
            steps += 1
        
        return steps
                
                

