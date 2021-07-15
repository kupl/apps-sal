import math

X = int(input())

n, m = 0, 100

while True:
    m += m // 100
    n += 1
    if X <= m:
        print(n)
        break

