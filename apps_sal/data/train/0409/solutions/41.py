class Solution:

    def low_high(self, arr):
        low = 0
        mhigh = 0
        high = 0
        peak = 0
        s = 0
        for i in range(len(arr)):
            s += arr[i]
            if s > high:
                high = s
            if s > mhigh:
                mhigh = s
            if s < low:
                low = s
                high = s
            if high - low > peak:
                peak = high - low
        return (low, high, peak, mhigh)

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        (low, high, peak, mhigh) = self.low_high(arr)
        print((low, high, peak, mhigh))
        s = sum(arr)
        print(s)
        if k == 1:
            return peak % 1000000007
        elif s > 0:
            return (max(k - 2, 0) * s + mhigh + (s - low)) % 1000000007
        elif s <= 0:
            return max(peak, mhigh + (s - low), s - low, 0) % 1000000007
