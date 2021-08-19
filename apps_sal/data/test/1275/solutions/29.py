(n, k) = map(int, input().split())


def f(a, b):
    return max(min(b - 1, 2 * a + 1 - b), 0)


ans = 0
for i in range(2, 2 * n + 1):
    ans += f(n, i) * f(n, i - k)
print(ans)
