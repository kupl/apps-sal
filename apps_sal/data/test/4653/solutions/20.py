t = int(input())
for i in range(t):
    (n, k) = list(map(int, input().split()))
    m = n % k
    print(n - m + min(k // 2, m))
