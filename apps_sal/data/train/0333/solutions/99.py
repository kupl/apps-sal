class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        if n == 2:
            return 1
        
        arr_f = []
        prev = None
        repeat = 0
        for num in arr:
            if num == prev:
                if repeat == 2:
                    continue
                repeat += 1
            else:
                prev = num
                repeat = 0
            arr_f.append(num)
        n = len(arr_f)
        
        idx_by_num = defaultdict(list)
        for i in range(n):
            idx_by_num[arr_f[i]].append(i)
        
        q = [(0, n-1)]
        visited = set([n-1])
        while q:
            step, cidx = q.pop(0)
            if cidx == 0:
                return step
            
            if cidx - 1 not in visited:
                visited.add(cidx - 1)
                q.append((step + 1, cidx - 1))
            if cidx + 1 < n and cidx + 1 not in visited:
                visited.add(cidx + 1)
                q.append((step + 1, cidx + 1))
            
            for same_v_idx in idx_by_num[arr_f[cidx]]:
                if same_v_idx not in visited:
                    visited.add(same_v_idx)
                    q.append((step + 1, same_v_idx))
            
        

