class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:

        NN, dd = N, 0
        nums = []
        while(NN):
            dd += 1
            nums.append(NN % 10)
            NN //= 10
        nums.reverse()

        numbers = 0
        for i in range(dd - 1):
            numbers += 9 * (math.factorial(9) // math.factorial(9 - i))

        already_visited_digits = set()

        def fac2(n, k):
            return math.factorial(n) // math.factorial(n - k)

        for i, n in enumerate(nums):
            k = 0
            for j in range((1 if i == 0 else 0), (n + 1 if i == dd - 1 else n)):
                if(j in already_visited_digits):
                    continue
                k += 1
            numbers += k * fac2(10 - i - 1, dd - i - 1)
            if n in already_visited_digits:
                break
            already_visited_digits.add(n)

        return N - numbers
