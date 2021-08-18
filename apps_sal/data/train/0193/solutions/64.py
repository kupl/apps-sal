class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        if len(set(arr)) == 1:
            return 1
        maps = {x: 0 for x in set(arr)}
        for x in arr:
            maps[x] += 1
        maps = sorted(list(maps.items()), key=lambda x: x[1], reverse=True)
        mincount = len(arr) // 2
        ans = 0
        currLength, sub = len(arr), 9
        for x in range(len(maps)):
            key, val = maps[x]
            if currLength > mincount:
                currLength -= val
                ans += 1
            else:
                return ans
