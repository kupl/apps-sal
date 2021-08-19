class Solution:

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = float('inf')
        high = float('-inf')
        for day in bloomDay:
            low = min(low, day)
            high = max(high, day)
        good = set()
        i = 0
        while low < high:
            guess = low + high >> 1
            count = 0
            boquets = 0
            for day in bloomDay:
                if day <= guess:
                    count += 1
                    if count == k:
                        boquets += 1
                        count = 0
                        if boquets == m:
                            break
                else:
                    count = 0
                day += 1
            if boquets < m:
                low = guess + 1
            else:
                good.add(guess)
                high = guess
        else:
            if not good:
                count = 0
                boquets = 0
                for day in bloomDay:
                    if day <= high:
                        count += 1
                        if count == k:
                            boquets += 1
                            count = 0
                            if boquets == m:
                                return high
                    else:
                        count = 0
                    day += 1
        return min(good) if good else -1
