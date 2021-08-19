class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def binarySearch(bloomDay, m, k, smallest, longest):
            waitDay = (smallest + longest) // 2
            totalCount = 0
            currentCount = 0
            # print(\"-=-=-=-=-=-=-=-=-=-=-=-=-=\")
            # print(smallest)
            # print(longest)
            for i in range(len(bloomDay)):
                if bloomDay[i] <= waitDay:
                    currentCount += 1
                else:
                    currentCount = 0

                if currentCount == k:
                    totalCount += 1
                    currentCount = 0
            if totalCount >= m:
                if smallest == waitDay:
                    return waitDay
                else:
                    checkSmaller = binarySearch(bloomDay, m, k, smallest, waitDay - 1)
                    if checkSmaller != -1:
                        return checkSmaller
                    else:
                        return waitDay
            else:
                if waitDay == longest:
                    return -1
                else:
                    return binarySearch(bloomDay, m, k, waitDay + 1, longest)

        if m * k > len(bloomDay):
            return -1
        else:
            return binarySearch(bloomDay, m, k, 0, max(bloomDay))
