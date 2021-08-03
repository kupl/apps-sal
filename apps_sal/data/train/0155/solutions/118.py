class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        def dp(arr, d, dic, i, n):

            if(dic[i] != None):
                return dic[i]

            maximum = 1

            upreached = False
            downreached = False

            for p in range(1, d + 1):

                if(i + p < n and not upreached):

                    if(arr[i + p] >= arr[i]):
                        upreached = True

                    else:
                        maximum = max(maximum, 1 + dp(arr, d, dic, i + p, n))

                if(i - p >= 0 and not downreached):

                    if(arr[i - p] >= arr[i]):
                        downreached = True

                    else:
                        maximum = max(maximum, 1 + dp(arr, d, dic, i - p, n))

                if(upreached and downreached):
                    break

            dic[i] = maximum

            return maximum

        n = len(arr)

        dic = [None] * n

        maximum = 0

        for i in range(n):

            maximum = max(maximum, dp(arr, d, dic, i, n))

        return maximum
