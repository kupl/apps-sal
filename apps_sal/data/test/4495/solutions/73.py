a, b, x = map(int, input().split())
ans = b // x - a // x
if a % x == 0:
    print(ans + 1)
else:
    print(ans)
