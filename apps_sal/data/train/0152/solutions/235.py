class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position = sorted(position)

        def isvalid(gap, m):
            j = 0
            for i in range(len(position)):
                if(position[i] - position[j] >= gap):
                    m -= 1
                    j = i
                    if m == 0:
                        return True
            return False

        low, high = 1, position[-1]
        sem = 0
        while(low <= high):
            mid = (high + low) // 2
            if isvalid(mid, m - 1):
                sem = mid
                low = mid + 1
            else:
                high = mid - 1

        return sem
