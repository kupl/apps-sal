class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1: return 0
        dictor = collections.defaultdict(list)
        queue = collections.deque([(0, 0)])
        
        for i in range(n):
            dictor[arr[i]].append(i)
        
        
        seen = set([0, n-1])
        while queue:
            idx, step = queue.popleft()
            indexes = dictor[arr[idx]]
            for i in indexes:
                if i == n - 1:
                    return step + 1
                if i not in seen:
                    queue.append((i, step + 1))
                    seen.add(i)
            del dictor[arr[idx]]
            
            for di in [-1, 1]:
                new_i = idx + di
                if new_i == n - 1:
                    return step + 1
                if 0 <= new_i < len(arr) and new_i not in seen:
                    queue.append((new_i, step + 1))
                    seen.add(new_i)
        return -1
                    

