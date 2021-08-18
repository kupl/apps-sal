class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        s = -1
        distMax = 0

        while s < len(seats) - 1:
            print('s: ', s)
            for e in range(s + 1, len(seats)):
                print('e: ', e)
                if seats[e] == 1:
                    if s == -1:
                        distMax = max(distMax, e)
                    else:
                        distMax = max(distMax, (e - s) // 2)
                    s = e
                    break
                elif e == len(seats) - 1:
                    distMax = max(distMax, len(seats) - 1 - s)
                    s = e

        return distMax
