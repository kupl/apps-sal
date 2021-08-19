from sys import stdin as fin
nums = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
(a, b) = map(int, fin.readline().split())
(result, last) = (0, 0)
for x in range(a, b + 1):
    dig = x % 10
    if not dig or not last:
        last = 0
        while x:
            (x, dig) = divmod(x, 10)
            last += nums[dig]
    else:
        last += nums[dig] - nums[dig - 1]
    result += last
print(result)
