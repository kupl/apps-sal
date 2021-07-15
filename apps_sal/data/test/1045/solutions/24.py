__author__ = 'valeriy.shevchuk'

n = int(input())

level = 1
prev = 1
sum = 1


while sum <= n:
    level += 1
    prev += level
    sum += prev

print(level - 1)
