class Solution:

    def maxDistToClosest(self, seats: List[int]) -> int:
        (count0, mmax, dist, start) = (0, 0, 0, True)
        for (i, e) in enumerate(seats):
            if e == 0:
                count0 += 1
                if i == len(seats) - 1:
                    dist = count0
            else:
                if count0 > 0:
                    if start:
                        dist = count0
                    else:
                        dist = (count0 + 1) // 2
                count0 = 0
                start = False
            mmax = max(dist, mmax)
        return mmax
