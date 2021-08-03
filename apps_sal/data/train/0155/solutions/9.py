class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        def dfs(i):
            if i in cache:
                return cache[i]
            cache[i] = 1
            for neigh in g[i]:
                cache[i] = max(cache[i], 1 + dfs(neigh))
            return cache[i]

        g = defaultdict(set)
        for i in range(len(arr)):
            for x in range(1, d + 1):
                if i - x >= 0 and arr[i - x] < arr[i]:
                    g[i].add(i - x)
                else:
                    break
            for x in range(1, d + 1):
                if i + x < len(arr) and arr[i + x] < arr[i]:
                    g[i].add(i + x)
                else:
                    break
        cache = {}
        for i in range(len(arr)):
            dfs(i)
        return max(cache.values())
        '''
        mjump = 0
        for i, x in enumerate(arr):
            top = i
            bottom = i
            while top+1 < len(arr) and x>arr[top+1]:
                top += 1
            while bottom-1 >= 0 and x>arr[bottom-1]:
                bottom -=1
            newarr = arr[bottom:top+1]
            
            jump =[x]
            value = x-1
            while value>=min(newarr):
                if value < jump[-1]-d:
                    break
                elif value in newarr:
                    jump.append(value)
                value -= 1
            
            print(jump)
            mjump = max(mjump, len(jump))
        
        return mjump
        '''
