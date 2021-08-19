t = int(input())
while t:
    (n, k) = map(int, input().split())
    print(n - max(0, n % k - k // 2))
    t -= 1
