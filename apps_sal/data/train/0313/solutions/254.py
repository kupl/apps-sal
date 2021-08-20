class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        sorted_bloomDay = sorted(set(bloomDay))
        left = 1
        right = len(sorted_bloomDay)
        ret = -1
        while left <= right:
            middle = (left + right) // 2 - 1
            bouquets_left = m
            flowers_left = k
            search_right = True
            for i in range(len(bloomDay)):
                if bloomDay[i] <= sorted_bloomDay[middle]:
                    flowers_left -= 1
                    if flowers_left == 0:
                        bouquets_left -= 1
                        if bouquets_left == 0:
                            ret = sorted_bloomDay[middle]
                            search_right = False
                            break
                        else:
                            flowers_left = k
                else:
                    flowers_left = k
            if search_right:
                left = middle + 2
            else:
                right = middle
        return ret
