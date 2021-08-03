class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        max_sums = [0] * len(arr)

        for i in range(len(arr)):

            if i <= k - 1:

                max_sums[i] = (i + 1) * max(arr[:i + 1])

            else:

                res = 0

                for j in range(1, k + 1):

                    first = max_sums[i - j]
                    second = j * max(arr[i - j + 1:i + 1])

                    #print(i, j)
                    #print(arr[:i-j+1], arr[i-j+1:i+1])
                    # print(\"first, second \", first, second)

                    res = max(res, first + second)

                max_sums[i] = res

            # print(max_sums)

        # print(max_sums)

        return max_sums[-1]
