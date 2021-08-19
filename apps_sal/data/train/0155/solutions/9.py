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
        '\n        mjump = 0\n        for i, x in enumerate(arr):\n            top = i\n            bottom = i\n            while top+1 < len(arr) and x>arr[top+1]:\n                top += 1\n            while bottom-1 >= 0 and x>arr[bottom-1]:\n                bottom -=1\n            newarr = arr[bottom:top+1]\n            \n            jump =[x]\n            value = x-1\n            while value>=min(newarr):\n                if value < jump[-1]-d:\n                    break\n                elif value in newarr:\n                    jump.append(value)\n                value -= 1\n            \n            print(jump)\n            mjump = max(mjump, len(jump))\n        \n        return mjump\n        '
