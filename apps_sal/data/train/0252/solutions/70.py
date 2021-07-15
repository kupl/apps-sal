class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        items = []
        for i, num in enumerate(ranges):
            items.append((max(0, i - num), min(i + num, n)))
        res = 0
        right = 0
        items.sort()
        i = 0
        while i < len(items):
            farreach = right
            while i < len(items) and items[i][0] <= right:
                farreach = max(farreach, items[i][1])
                i += 1
            
            if farreach == right:
                return -1
            res += 1
            if farreach >= n:
                return res
            right = farreach
        
        return -1
