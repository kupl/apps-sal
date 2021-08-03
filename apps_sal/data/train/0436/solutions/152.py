class Solution:
    def minDays(self, n: int) -> int:
        day_dict = set([n])
        day = 0
        while True:
            day_next = []
            for num in day_dict:
                if num % 2 == 0:
                    day_next.append(num // 2)
                if num % 3 == 0:
                    day_next.append(num // 3)
                day_next.append(num - 1)
            day += 1
            day_dict = set(day_next)
            if 0 in day_next:
                return day
        return
