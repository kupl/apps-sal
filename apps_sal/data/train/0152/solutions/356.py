def possible(min_diff, arr, m):
    start = 0
    total = 1
    end = 1
    while end < len(arr):
        if arr[end] - arr[start] >= min_diff:
            total += 1
            start = end
        end += 1
    if total >= m:
        return True
    return False


class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        ans = -1
        low = 1
        high = 10 ** 9
        while low <= high:
            mid = (low + high) // 2
            if possible(mid, position, m):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return ans
