n = int(input())
x = str(n + n - 1)
if x.count('9') == len(x):
    m = len(x)
else:
    m = len(x) - 1
m = '9' * m


def f(x):
    if n + n - 1 < x:
        return 0
    if x <= n:
        if x % 2 == 0:
            return max(x // 2 - 1, 0)
        return x // 2
    if x % 2 == 0:
        x //= 2
        return max(min(n - x, x - 1), 0)
    return max(min(n - x // 2, x // 2), 0)


ans = 0
for i in range(9):
    s = int(str(i) + m)
    ans += f(s)
print(ans)
