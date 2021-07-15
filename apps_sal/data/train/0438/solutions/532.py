class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        vals = [0] * (len(arr) + 2)
        intervals = [0, len(arr) + 1]
        for idx in reversed(list(range(len(arr)))):
            bit = arr[idx]
            lo = 0
            hi = len(intervals)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if intervals[mid] >= bit:
                    hi = mid
                else:
                    lo = mid + 1
                    
            leftLen = bit - intervals[lo - 1] - 1
            rightLen = intervals[lo] - bit - 1
            if leftLen == m or rightLen == m:
                return idx
            if intervals[lo] - intervals[lo - 1] - 1 > m:
                intervals.insert(lo, bit)
        return -1

