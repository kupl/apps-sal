n, k = map(int, input().split())
ans = 0


def f(a, b):
    return max(min(b - 1, 2 * a + 1 - b), 0)


for x in range(2, 2 * n + 1):
    ans += f(n, x) * f(n, x - k)
print(ans)
