T = int(input())
for _ in range(T):
    n, k = list(map(int, input().split()))
    print(n // k * k + min(n % k, int(k / 2)))
