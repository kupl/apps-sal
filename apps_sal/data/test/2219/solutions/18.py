t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    res = 0
    while n > 0:
        res += n % k
        n -= n % k
        if n > 0:
            n = n // k
            res += 1
    print(res)
