(n, k, m) = map(int, input().split())
a = map(int, input().split())
ans = n * m - sum(a)
if ans < 0:
    print(0)
elif ans > k:
    print(-1)
else:
    print(ans)
