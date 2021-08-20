class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        for (i, val) in enumerate(ranges):
            if i - val < 0:
                ranges[0] = max(i + val, ranges[0])
            else:
                ranges[i - val] = max(val * 2, ranges[i - val])
        i = 0
        prev = -1
        counter = 0
        while i != prev:
            distance = ranges[i]
            if i + distance >= n:
                return counter + 1
            maxIndex = i
            for j in range(i + distance + 1):
                if j + ranges[j] >= maxIndex + ranges[maxIndex]:
                    maxIndex = j
                j += 1
            prev = i
            i = maxIndex
            counter += 1
        return -1
