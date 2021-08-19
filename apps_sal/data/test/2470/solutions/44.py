class Solution:
    def binary_search_right(self, arr, l, r, t):
        while l < r:
            m = l + (r - l) // 2
            if arr[m] <= t:
                l = m + 1
            else:
                r = m
        return l

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        dp = {}

        def help(i1, i2):
            if i1 == len(arr1):
                return 0

            if i1 != 0:
                key = (i1, i2, arr1[i1 - 1])
            else:
                key = (i1, i2, None)

            if key in dp:
                return dp[key]

            # print(key)

            # all possible results
            pos = []

            # don't make changes here
            if i1 == 0 or arr1[i1 - 1] < arr1[i1]:
                res = help(i1 + 1, i2)
                if res != -1:
                    pos.append(res)

            if i1 != 0:
                # make change
                i2 = self.binary_search_right(arr2, i2, len(arr2), arr1[i1 - 1])
                if i2 != len(arr2):
                    tmp = arr1[i1]
                    arr1[i1] = arr2[i2]
                    res = help(i1 + 1, i2 + 1)
                    if res != -1:
                        pos.append(res + 1)
                    arr1[i1] = tmp
            else:
                # make change
                if i2 < len(arr2) and arr2[i2] < arr1[i1]:
                    tmp = arr1[i1]
                    arr1[i1] = arr2[i2]
                    res = help(i1 + 1, i2 + 1)
                    if res != -1:
                        pos.append(res + 1)
                    arr1[i1] = tmp

            if len(pos) == 0:
                dp[key] = -1
            else:
                dp[key] = min(pos)
            return dp[key]

        return help(0, 0)
