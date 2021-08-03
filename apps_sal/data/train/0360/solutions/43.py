class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def package(weights, limit):
            kk = 0
            count = 1
            for i in range(len(weights)):
                kk = kk + weights[i]

                if kk > limit:
                    kk = weights[i]
                    count = count + 1

            return count

        lindex = max(weights)
        rindex = lindex * len(weights) // D

        while (lindex < rindex):

            mid = lindex + (rindex - lindex) // 2

            capacity = mid
            Dstar = package(weights, capacity)

            if Dstar > D:
                lindex = mid + 1
            else:
                rindex = mid

        return lindex
