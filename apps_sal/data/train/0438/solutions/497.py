class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == m:
            return m
        
        intervals = [[1, len(arr)]]
        
        for i in range(len(arr)-1, -1, -1):
            remove = arr[i]
            l, r = 0, len(intervals)-1
            while l <= r:
                mid = l + (r - l)//2
                if intervals[mid][0] > remove:
                    r = mid - 1
                else:
                    l = mid + 1
            interval = list(intervals[r])
            if interval[0] == remove:
                intervals[r][0] = intervals[r][0] + 1
                if intervals[r][1] - intervals[r][0] + 1 == m:
                    return i
            elif interval[1] == remove:
                intervals[r][1] = intervals[r][1] - 1
                if intervals[r][1] - intervals[r][0] + 1 == m:
                    return i
            else:
                intervals.insert(r, list(interval))
                intervals[r][1] = remove - 1
                intervals[r+1][0] = remove + 1
                if (intervals[r][1] - intervals[r][0] + 1 == m) or (intervals[r+1][1] - intervals[r+1][0] + 1 == m):
                    return i
        return -1
                
            
            

