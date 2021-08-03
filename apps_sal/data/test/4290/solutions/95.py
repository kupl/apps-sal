n, m = map(int, input().split())
ans = 0


def com2(x):
    return x * (x - 1) // 2


if n >= 2:
    ans += com2(n)
if m >= 2:
    ans += com2(m)
print(ans)
