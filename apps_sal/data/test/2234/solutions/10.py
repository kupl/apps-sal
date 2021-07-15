import math

t = int(input())

for p in range(t):
    n, k = map(int, input().split())
    if k > n:
        print(k - n)
    elif k%2 == n%2:
        print(0)
    else:
        print(1)
