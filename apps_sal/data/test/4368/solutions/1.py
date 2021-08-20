(N, K) = map(int, input().split())
n = N
i = 1
while 1 > 0:
    n = n // K
    if n == 0:
        print(i)
        break
    i += 1
