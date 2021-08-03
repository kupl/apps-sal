from array import array


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        if k == 0:
            return 0

        min_d, max_d = bloomDay[0], bloomDay[0]

        for d in bloomDay:
            if d > max_d:
                max_d = d
            if d < min_d:
                min_d = d

        def possible_bouquets(day):
            bouquets = 0
            flower_count = 0
            i = 0
            while i < len(bloomDay):
                if bloomDay[i] <= day:
                    flower_count += 1

                    if flower_count == k:
                        bouquets += 1
                        flower_count = 0
                else:
                    flower_count = 0
                i += 1
            return bouquets

        possible_days = -1
        day_guess = (min_d + max_d) // 2

        while min_d <= max_d:
            bouquets = possible_bouquets(day_guess)
            # print(f\"{day_guess}:{bouquets}\")
            if bouquets >= m:
                max_d = day_guess - 1
                possible_days = day_guess
            else:
                min_d = day_guess + 1

            day_guess = (min_d + max_d) // 2

        return possible_days
