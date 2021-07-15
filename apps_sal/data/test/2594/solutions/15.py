from math import sqrt

t = int(input())


for qq in range(t):
    n, m = [int(i) for i in input().split()]
    print((n * m) // 2 + (n * m) % 2)

