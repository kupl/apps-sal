t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    z = n // k
    n -= z * k
    print(z * k + min(n, k // 2))
