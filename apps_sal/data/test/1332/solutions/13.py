a, b, c, d, e = map(int, input().split())
ans = a + b + c + d + e
if ans % 5 != 0 or ans // 5 < 1:
    print(-1)
else:
    print(ans // 5)
