import sys
3


n = int(input())

nums = []
while n != 0:
    num = 0
    pow10 = 1
    while n >= pow10:
        if n % (pow10 * 10) >= pow10:
            num += pow10
            n -= pow10
        pow10 *= 10
    nums.append(num)

print(len(nums))
print(" ".join(map(str, nums)))
