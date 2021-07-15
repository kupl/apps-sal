class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        parents = list(range(len(arr) + 1))
        group = [0] * (len(arr)  + 1)
        counter = collections.Counter()
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                parents[py] = px
                counter[group[px]] -= 1
                counter[group[py]] -= 1
                group[px] += group[py]
                counter[group[px]] += 1
            return
        
        visited = set()
        ans = -1
        
        for i in range(len(arr)):
            x = arr[i]
            group[x] = 1
            counter[1] += 1
            for y in [x - 1, x + 1]:
                if y in visited:
                    union(x, y)
            visited.add(x)
            
            if counter[m] > 0:
                ans = i + 1
        return ans
