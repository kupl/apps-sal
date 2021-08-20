class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def working(mid: int):
            prev_stall = 0
            stall = 1
            for i in range(1, m):
                while position[stall] - position[prev_stall] < mid:
                    stall += 1
                    if stall == len(position):
                        return False
                prev_stall = stall
            return True
        L = max(position)
        low = 1
        high = int(L / (m - 1))
        largest = 0
        position = sorted(position)
        while low <= high:
            mid = int((low + high) / 2)
            if working(mid):
                if mid < int(L / (m - 1)):
                    low = mid + 1
                else:
                    largest = max(largest, mid)
                    break
                largest = max(largest, mid)
            elif mid > 0:
                high = mid - 1
        return largest
