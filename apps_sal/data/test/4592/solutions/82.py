import math
import collections
N = int(input())
nums = [i for i in range(2, N + 1)]


def prime_factorization(num):
    sqrt_num = math.sqrt(num)
    prime_numbers = []
    for i in range(2, int(sqrt_num) + 1):
        while num % i == 0:
            num = num / i
            prime_numbers.append(i)
    if num != 1:
        prime_numbers.append(int(num))
    return prime_numbers


nums_counter = {}
for num in nums:
    prime_numbers = prime_factorization(num)
    for prime_num in prime_numbers:
        if prime_num in nums_counter:
            nums_counter[prime_num] += 1
        else:
            nums_counter[prime_num] = 1
ans = 1
for (key, value) in list(nums_counter.items()):
    ans *= value + 1
    ans %= 10 ** 9 + 7
print(ans)
