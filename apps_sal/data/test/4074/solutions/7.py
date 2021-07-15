import math

T = int(input())


def divs(n):
    d = []
    for i in range(1, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            d.extend([i, n//i])
    return sorted(d)

for t in range(T):
    N, K = [int(_) for _ in input().split()]
    for d in divs(N):
        if N / d <= K:
            print(d)
            break

