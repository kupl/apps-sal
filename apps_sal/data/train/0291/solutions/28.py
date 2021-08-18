class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        o = []
        score = 0
        tmp = 0
        pa, no = 0, 0
        check = []

        for el in arr:
            tmp += el

            if tmp % 2 == 0:
                pa += 1
                check.append(0)
            else:
                no += 1
                check.append(1)

            o.append((pa, no))

        score = 0

        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                score += 1

            if check[i - 1] == 0 or i == 0:
                score += o[-1][1] - o[i][1]
            else:
                score += o[-1][0] - o[i][0]

        mod = 10**9 + 7
        return score % mod
