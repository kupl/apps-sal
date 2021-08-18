class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        n = len(arr)

        p1 = p2 = -1

        for i in range(1, n):
            if arr[i] < arr[i - 1]:

                p2 = i

                if p1 == -1:
                    p1 = i

        if p1 == -1:
            return 0

        def chk(l):

            nonlocal p1
            nonlocal p2

            if l >= p2:
                return True

            n = len(arr)

            for i in range(n):

                if i > p1:
                    return False

                if i + l >= n:
                    return True

                if i + l < p2:
                    continue

                if arr[i - 1] <= arr[i + l]:
                    return True

            return False

        l = 0
        r = n

        while l < r:

            mid = (l + r) // 2

            if chk(mid):
                r = mid
            else:
                l = mid + 1

        return l
