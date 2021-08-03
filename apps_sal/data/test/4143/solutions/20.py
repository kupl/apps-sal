from math import ceil

n = int(input())
a = [int(input()) for _ in range(5)]

print((ceil(n / min(a)) + 4))
