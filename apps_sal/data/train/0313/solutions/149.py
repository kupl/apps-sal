class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)

        def get_num_boquets(wait_days):
            i = 0
            while i < n and bloomDay[i] > wait_days:
                i += 1
            # i: index of first available flower
            j = i
            count = 0
            while j < n:
                while j < n and bloomDay[j] <= wait_days:
                    j += 1
                j -= 1  # index of last available flower in the adjacent subarray
                count += (j - i + 1) // k
                i = j + 1
                while i < n and bloomDay[i] > wait_days:
                    i += 1
                # i: index of first available flower
                j = i
            return count
        start = 1
        end = max(bloomDay)
        while start < end:
            mid = start + (end - start) // 2
            #print(mid, get_num_boquets(mid))
            if get_num_boquets(mid) >= m:
                # wait is too long, or just right
                end = mid
            else:
                # wait is too short
                start = mid + 1
        if start >= 1 and start <= max(bloomDay) and get_num_boquets(start) >= m:
            return start
        else:
            return -1
