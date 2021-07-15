class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        if m == len(arr): return m
        d = {v: i + 1 for i, v in enumerate(arr)}
        latest = -1
        
        i, j = 1, m
        max_stack = collections.deque()
        
        for t in range(i, j + 1):
            while max_stack and max_stack[-1] < d[t]:
                max_stack.pop()
            max_stack.append(d[t])
        
        while j <= len(arr):
            in_max = max_stack[0]
            
            if in_max < d.get(i - 1, float('inf')) and in_max < d.get(j + 1, float('inf')):
                latest = max(latest, min(d.get(i - 1, float('inf')), d.get(j + 1, float('inf'))) - 1)
            
            if d[i] == max_stack[0]:
                max_stack.popleft()
            
            i += 1
            j += 1
            
            if j <= len(arr):
                while max_stack and max_stack[-1] < d[j]:
                    max_stack.pop()
                max_stack.append(d[j])

        return latest
