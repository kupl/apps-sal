class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        max = 0
        min = 0
        index = 0
        total = 0
        while max < n:
            for i in range(index, len(ranges)):
                left = i - ranges[i]
                right = i + ranges[i]
                if left <= min and right > max:
                    max = right
                    index = i
            if min == max:
                return -1
            total += 1
            min = max
        return total
