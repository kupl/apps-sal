class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # up till N // 2 + 1
        # output is at least 1
        # if N == 1 or N == 2:
        #     return 1
        # start = N // 2 + 1
        # result = 1
        # candidates = [i for i in range(start,0,-1)]
        # n = 2
        # i = 0
        # while True:
        #     if i+n > start:
        #         return result
        #     # print(candidates[i:i+n])
        #     temp_sum = (candidates[i] + candidates[i+n-1]) * n / 2
        #     if temp_sum == N:
        #         result += 1
        #         i += 1
        #         n += 1
        #     elif temp_sum > N:
        #         i += 1
        #     else:
        #         n += 1
        res = 1
        i = 3
        while N % 2 == 0:
            N /= 2
        while i * i <= N:
            count = 0
            while N % i == 0:
                N /= i
                count += 1
            res *= count + 1
            i += 2
        return res if N == 1 else res * 2
            

