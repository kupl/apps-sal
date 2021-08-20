q = int(input())
for _ in range(q):
    (k, n, a, b) = map(int, input().split())
    ans = (k - b * n - 1) // (a - b)
    if b * n >= k:
        print(-1)
    else:
        print(min(ans, n))
