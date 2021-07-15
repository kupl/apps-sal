from sortedcontainers import SortedList

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        sl = SortedList()
        n = len(arr)
        if n == m:
            return n
        s = n
        while s >= 1:
            s -= 1
            if len(sl) == 0:
                if n-arr[s] == m or arr[s] - 1 == m:
                    return s
            else:
                idx = sl.bisect_left(arr[s])
                if idx == 0:
                    if arr[s] - 1 == m or sl[idx] - arr[s] - 1 == m:
                        return s
                elif idx == len(sl):
                    if n - arr[s] == m or arr[s] - sl[idx-1] - 1 == m:
                        return s
                else:
                    if arr[s] - sl[idx-1] - 1 == m or sl[idx] - arr[s] - 1 == m:
                        return s
            sl.add(arr[s])
        return -1
