N = int(input())

nums = list(n for n in range(1, N + 1) if n % 2 == 1)
len_nums = len(nums)

divisors = []
for i in range(len_nums):
    n = 1
    divisor = 0
    while n <= N:
        if nums[i] % n == 0:
            divisor += 1
        n += 1
    divisors.append(divisor)

print(divisors.count(8))
