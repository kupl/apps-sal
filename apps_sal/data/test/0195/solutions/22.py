(a, b, c, n) = list(map(int, input().split()))
ans = n - (a + b - c)
if ans < 1 or c > a or c > b or (a > n) or (b > n) or (c > n):
    print(-1)
else:
    print(ans)
