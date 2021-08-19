class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        ages = sorted(ages)
        print(ages)

        def bound(a):
            low = a // 2 + 8
            hi = a
            return (min(low, a), hi)

        def getlow(v):
            (lo, hi) = (0, len(ages))
            while lo < hi:
                mid = (lo + hi) // 2
                if ages[mid] >= v:
                    hi = mid
                else:
                    lo = mid + 1
            return hi

        def getupper(v):
            (lo, hi) = (0, len(ages))
            while lo < hi:
                mid = (lo + hi) // 2
                if ages[mid] <= v:
                    lo = mid + 1
                else:
                    hi = mid
            return hi - 1
        count = 0
        for i in range(len(ages)):
            if ages[i] <= 14:
                continue
            (minv, maxv) = bound(ages[i])
            c = getupper(maxv) - getlow(minv)
            count += c
        p = 115
        return count
