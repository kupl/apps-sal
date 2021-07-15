class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        hMap = {}
        if not tree:
            return 0
            
        maxCount = 0
        count = 0
        for i in range(len(tree)):
            hMap[tree[i]] = i
            
            if len(hMap) <= 2:
                count += 1
                maxCount = max(count, maxCount)
            else:
                j = sys.maxsize
                r = None
                for k in hMap:
                    if hMap[k] < j:
                        r = k
                        j = hMap[k]
                hMap.pop(r, None)
                count = i - j
                
            # print(tree[i], hMap, count, maxCount)
                
        return maxCount
