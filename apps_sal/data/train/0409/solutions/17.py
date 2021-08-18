class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = arr[0]
        ans = dp
        sums = sum(arr)
        begin, maxbegin = 0, 0
        end, maxend = 0, 0
        for i in range(1, n * min(2, k)):
            cur = arr[i % n]
            if dp + cur >= cur:
                dp = dp + cur
                end = i
            else:
                dp = cur
                begin, end = i, i
            if dp > ans:
                ans = dp
                maxbegin = begin
                maxend = i
        if k == 1:
            return ans if ans > 0 else 0
        if ans < 0:
            return 0
        if maxend % n < maxbegin or maxend < n:
            return ans % (10**9 + 7)
        else:
            return (ans + sums * (k - 2)) % (10**9 + 7)
