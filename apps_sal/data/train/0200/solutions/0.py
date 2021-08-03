class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]  # initializing a Fibonacci table with F[0] and F[1]
        i = 1  # index that will represent the last filled index of table
        temp = fib[0] + fib[1]  # initial value of values to be appended
        while temp < k:  # we keep filling table until temp >= k
            fib.append(temp)  # add the current value to the table
            i += 1  # increase i by 1 to keep track of the last filled index
            temp = fib[i] + fib[i - 1]  # calculate new temp
        fib.append(temp)  # to cover case temp == k, we append the last value >= k

        ans = 0  # initializing answer value with 0
        j = -1  # placeholder to represent last checked Fibonacci table index
        while k > 0:  # keep repeating until k <= 0
            temp = fib[j]  # get the biggest number available
            j -= 1  # decrease j by 1 since we tried the last number

            if temp <= k:
                ans += 1
                k -= temp

        return ans
