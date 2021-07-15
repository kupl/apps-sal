import math
import collections
N = int(input())
# N!の約数の個数を10**9+7で割ったあまりを出す
nums = [i for i in range(2, N + 1)]


def prime_factorization(num):
    sqrt_num = math.sqrt(num)
    prime_numbers = []
    for i in range(2, int(sqrt_num) + 1):
        # print(num)
        while num % i == 0:
            # print(num)
            num = num / i
            prime_numbers.append(i)
    if num != 1:
        prime_numbers.append(int(num))

    return prime_numbers


# print(nums)
nums_counter = {}
for num in nums:
    prime_numbers = prime_factorization(num)
    # print(prime_numbers)
    for prime_num in prime_numbers:
        # print(nums_counter)
        # print(prime_num in nums_counter)
        if prime_num in nums_counter:
            nums_counter[prime_num] += 1
        else:
            nums_counter[prime_num] = 1

ans = 1
for key, value in list(nums_counter.items()):
    ans *= (value + 1)
    ans %= 10**9 + 7

print(ans)

