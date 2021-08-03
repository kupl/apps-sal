n, k, m = map(int, input().split())
A = list(map(int, input().split()))

aim = n * m

p = sum(A)

if aim - p < 0:
    print(0)
elif aim - p > k:
    print(-1)
elif aim - p <= k:
    print(aim - p)
