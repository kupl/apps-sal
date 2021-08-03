class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def check(curr_day):
            ans = 0
            i = -1
            for j, day in enumerate(bloomDay):
                if day > curr_day:
                    ans += (j - 1 - i) // k
                    i = j
                if ans >= m:
                    return True
            ans += (len(bloomDay) - 1 - i) // k
            return ans >= m
        candidates = sorted(set(bloomDay))

        l, r = 0, len(candidates) - 1
        while r > l:
            mid = l + (r - l) // 2
            if check(candidates[mid]):
                r = mid
            else:
                l = mid + 1
        return candidates[l]
