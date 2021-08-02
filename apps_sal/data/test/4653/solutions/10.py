t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    if n % k <= k // 2:
        print(n)
    else:
        print((n // k) * k + k // 2)
