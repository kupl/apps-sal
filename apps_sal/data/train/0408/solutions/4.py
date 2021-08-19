def binsearch(arr, x):
    if x < arr[0]:
        return 0
    n = len(arr)
    if arr[n - 1] <= x:
        return n
    s = 0
    e = len(arr) - 1
    ret = n
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] <= x:
            s = mid + 1
        else:
            ret = mid
            e = mid - 1
    return ret


class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        n = len(arr)
        arr.sort()
        prefix = []
        prefix.append(arr[0])
        for i in range(1, n):
            prefix.append(prefix[i - 1] + arr[i])
        prefix.append(0)
        low = 0
        hi = arr[n - 1]
        minret = 1
        mindiff = sys.maxsize
        while low <= hi:
            mid = (low + hi) // 2
            x = binsearch(arr, mid)
            val = prefix[x - 1] + (n - x) * mid
            diff = abs(val - target)
            if diff == mindiff and mid < minret:
                minret = mid
            elif diff < mindiff:
                mindiff = diff
                minret = mid
            if val < target:
                low = mid + 1
            else:
                hi = mid - 1
        return minret
