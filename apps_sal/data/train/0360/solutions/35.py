class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def checkDays(capacity):
            days = 1
            cc = 0
            for num in weights:
                if cc == capacity:
                    cc = 0
                    days += 1
                if num > capacity:
                    return 999999
                cc += num
                if cc > capacity:
                    days += 1
                    cc = num
            return days
        hi = max(weights) * len(weights)
        low = 0
        while low < hi:
            guess = int((low + hi) / 2)
            print(low, hi, guess)
            d = checkDays(guess)
            if d > D:
                low = guess + 1
            else:
                hi = guess
        return low
