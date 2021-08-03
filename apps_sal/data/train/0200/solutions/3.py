class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        first = 1
        second = 1

        fib = []

        i = 0
        while True:
            if i == 0:
                fib.append(1)
            elif i == 1:
                fib.append(1)
            else:
                val = fib[i - 1] + fib[i - 2]
                if val > k:
                    break
                fib.append(val)
            i += 1
        print(fib)
        accum = 0
        ct = 0
        for i in range(len(fib) - 1, -1, -1):
            accum += fib[i]
            if accum == k:
                ct += 1
                break
            elif accum > k:
                accum -= fib[i]
            else:
                ct += 1
        return ct
