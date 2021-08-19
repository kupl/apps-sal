(a, b, c, n) = map(int, input().split())
ans = n - a - b + c
if ans < 1 or min(a, b) < c:
    print(-1)
else:
    print(ans)
