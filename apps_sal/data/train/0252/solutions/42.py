class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        minimum=0
        maximum=0
        total=0
        while maximum<n:
            for i in range(len(ranges)):
                left=i-ranges[i]
                right=i+ranges[i]
                if left<=minimum and right>maximum:
                    maximum=right
            if minimum==maximum:
                return -1
            minimum=maximum
            total+=1
        return total
