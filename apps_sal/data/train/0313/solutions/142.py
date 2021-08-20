class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        low = k
        high = min1 = max(bloomDay)
        while low <= high:
            mid = (low + high) // 2
            flag = sum1(mid, bloomDay, k)
            if flag >= m:
                high = mid - 1
                min1 = min(mid, min1)
            else:
                low = mid + 1
        return min1


def sum1(given, bloom, k):
    res = 0
    count = 0
    i = 0
    while i < len(bloom):
        if bloom[i] > given:
            i += 1
            count = 0
            continue
        while i < len(bloom) and bloom[i] <= given:
            count += 1
            i += 1
            if count == k:
                res += 1
                count = 0
    return res
