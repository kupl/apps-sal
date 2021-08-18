class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def isPossible(arr, n, C, mid):
            magnet = 1
            currPosition = arr[0]

            for i in range(1, n):

                if (arr[i] - currPosition >= mid):
                    magnet += 1

                    currPosition = arr[i]

                    if (magnet == C):
                        return True

            return False

        def binarySearch(n, C, arr):
            arr.sort(reverse=False)

            lo = 0

            hi = arr[n - 1]
            ans = 0

            while (lo <= hi):
                mid = int((lo + hi) / 2)

                if (isPossible(arr, n, C, mid) == False):
                    hi = mid - 1
                else:

                    ans = max(ans, mid)
                    lo = mid + 1

            return ans

        n = len(position)
        return binarySearch(n, m, position)
