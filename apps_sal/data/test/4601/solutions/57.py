(n, k) = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse=True)
if k >= n:
    print(0)
else:
    ans = 0
    for i in range(k, n):
        ans += h[i]
    print(ans)
