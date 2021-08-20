(n, k, m) = map(int, input().split())
a = list(map(int, input().split()))
a1 = sum(a)
ans = n * m - a1
if ans > k:
    print(-1)
elif ans < 0:
    print(0)
else:
    print(ans)
