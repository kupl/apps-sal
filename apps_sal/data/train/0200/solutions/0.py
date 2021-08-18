class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        i = 1
        temp = fib[0] + fib[1]
        while temp < k:
            fib.append(temp)
            i += 1
            temp = fib[i] + fib[i - 1]
        fib.append(temp)

        ans = 0
        j = -1
        while k > 0:
            temp = fib[j]
            j -= 1

            if temp <= k:
                ans += 1
                k -= temp

        return ans
