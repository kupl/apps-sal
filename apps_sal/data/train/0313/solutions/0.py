class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        flowersN = len(bloomDay)
        if flowersN < m * k:
            return -1

        def checkFlowers(x):
            count = 0
            gotFlowers = 0
            for num in bloomDay:
                if num <= x:
                    count += 1
                    if count == k:
                        gotFlowers += 1
                        count = 0
                else:
                    count = 0
            # print(gotFlowers, x, m)
            return gotFlowers >= m

        sortedDays = sorted(list(set(bloomDay)))
        l = 0
        r = len(sortedDays) - 1
        if checkFlowers(sortedDays[l]):
            return sortedDays[l]
        while l < r:
            mm = (l + r) // 2
            if checkFlowers(sortedDays[mm]):
                r = mm
            else:
                l = mm + 1
        return sortedDays[l]
