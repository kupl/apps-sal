class Solution:

    def checkDay(self, day, bloomDay, m, k) -> bool:
        (y, count) = (0, 0)
        for i in range(len(bloomDay)):
            if bloomDay[i] <= day:
                y += 1
            else:
                y = 0
            if y == k:
                count += 1
                y = 0
            if count == m:
                return True
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        bloomDay: Flower garden, elements are # of days required for that flower to bloom
        m: # of bouquets needed
        k: # of adjacent flowers needed in each bouquet
        First, check to see if mk>len(bloomDay). If so return -1
        Then, see how many days needed until mk flowers have bloomed
            Check to see if they are adjacent
            if so return days
            else maybe check how many adjacents are needed, or go to the next day

        """
        FN = m * k
        if FN > len(bloomDay):
            return -1
        (lastWorking, count, start, stop) = (-1, 0, 0, len(bloomDay))
        bloomed = sorted(bloomDay)
        print(bloomed)
        half = stop // 2
        while start <= half < stop:
            day = bloomed[half]
            print('Half: ', half, ', Day: ', day, ' || Bounds: ', start, ', ', stop)
            if self.checkDay(day, bloomDay, m, k):
                print('Day:  ', day, ' works')
                (lastWorking, stop) = (day, half)
            else:
                start = half + 1
            half = (start + stop) // 2
        return lastWorking
