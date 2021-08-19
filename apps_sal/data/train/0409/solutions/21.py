class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)

        lsum, max_lsum, min_lsum, max_sum, sum, max_rsum, rsum = 0, 0, 0, 0, 0, 0, 0
        for i in range(n):
            lsum += arr[i]
            max_lsum = max(lsum, max_lsum)  # FOR END
            min_lsum = min(lsum, min_lsum)  # FOR START

            sum += arr[i]
            sum = max(0, sum)
            max_sum = max(sum, max_sum)

            rsum += arr[n - 1 - i]
            max_rsum = max(rsum, max_rsum)

        if lsum < 0:
            return max(max_sum, max_rsum + max_lsum)

        if k == 1:
            return max_sum

        mod = 10 ** 9 + 7
        return max(lsum * k, lsum * (k - 2) + max_rsum + max_lsum) % mod


#[2,-5,1,0,-2,-2,2] [2,-5,1,0,-2,-2,2] [2,-5,1,0,-2,-2,2] [2,-5,1,0,-2,-2,2]
