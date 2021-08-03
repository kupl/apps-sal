import math
n = int(input())
nums = list(map(int, input().split()))


summ = 1
b = 1
mod = 10**9 + 7

for idx in range(1, n):
    temp = b * nums[idx - 1]
    gcd = math.gcd(temp, nums[idx])
    multiple = nums[idx] // gcd
    summ *= multiple

    b = b * nums[idx - 1] * multiple // nums[idx]
    summ += b
    summ %= mod

print(summ)
