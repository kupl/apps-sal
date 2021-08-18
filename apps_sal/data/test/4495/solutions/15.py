
a, b, x = map(int, input().split())

ans = (b // x) - ((a - 1) // x)
if ans < 0:
    ans = 0

print(ans)
