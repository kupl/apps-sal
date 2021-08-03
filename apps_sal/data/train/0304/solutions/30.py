class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()

        def count(a):
            i, j = 0, len(ages) - 1

            while i < j:
                k = (i + j + 1) // 2
                if ages[k] <= a:
                    i = k
                else:
                    j = k - 1

            u = i

            v = a // 2 + 7
            i, j = 0, len(ages) - 1

            while i < j:
                k = (i + j) // 2
                if ages[k] <= v:
                    i = k + 1
                else:
                    j = k

            l = i

            return u - l if l <= u else 0

        return sum(count(a) for a in ages)
