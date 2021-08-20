(a, b, x) = map(int, input().split())
ans = b // x + 1 - (a // x + 1)
if a % x == 0:
    ans += 1
print(ans)
