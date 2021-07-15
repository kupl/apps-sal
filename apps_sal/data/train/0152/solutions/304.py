class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def count(d):
            prev, tot = position[0], m-1
            for i in range(1, len(position)):
                if position[i] - prev >= d:
                    prev = position[i]
                    tot -= 1
                    if tot == 0: return True
            return False
        position.sort()
        low, high = 0, position[-1]-position[0]
        res = None
        while low <= high:
            mid = (low + high)//2
            if count(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res
            

