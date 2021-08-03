class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        #         if N == 1:
        #             return 1
        #         res = 1
        #         for i in range(2, floor(1 + N ** (0.5))):
        #             if N % i == 0:
        #                 if i % 2 == 1: # If i is odd, then we can form a sum of length i
        #                     res += 1
        #                 j = (N // i) # Check the corresponding N // i
        #                 if i != j and j % 2 == 1:
        #                     res += 1
        #         if N % 2 == 1: # If N is odd(2k + 1). Then N = k + k + 1, not included above
        #             res += 1

        #         return res

        #         if N == 1:
        #             return 1
        #         total = 1

        #         start = 1
        #         end = 1

        #         curr = 1
        #         while end <= ceil(N / 2):
        #             if curr == N:
        #                 total += 1
        #                 curr -= start
        #                 start += 1
        #             if curr < N:
        #                 end += 1
        #                 curr += end
        #             elif curr > N:
        #                 curr -= start
        #                 start += 1

        #         return total

        c, k = 0, 0
        while(k * (k + 1) / 2 < N):
            r = N - k * (k + 1) / 2
            if r % (k + 1) == 0:
                c += 1
            k += 1

        return c
