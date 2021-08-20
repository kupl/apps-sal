class Solution:

    def maxSubarraySumCircular(self, arr: List[int]) -> int:

        def maxsub(a, n):
            maxsum = a[0]
            currsum = 0
            for i in range(n):
                if currsum + a[i] > 0:
                    currsum += a[i]
                    maxsum = max(maxsum, currsum)
                else:
                    currsum = 0
                    maxsum = max(maxsum, a[i])
            return maxsum
        b = [i * -1 for i in arr]
        n = len(arr)
        s = sum(arr)
        ans2 = 0
        ans2 = maxsub(b, n)
        if s == -ans2:
            ans2 = -ans2
        return max(maxsub(arr, n), s + ans2)
