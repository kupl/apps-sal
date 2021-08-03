f, c, i = lambda x: x // 2, lambda x: x - f(x), lambda: map(int, input().split())
n, q = i()
res = ''
for _ in range(q):
    x, y = i()
    if (x + y) % 2 == 0:
        res += str(((f(x) * n - f(n) * (x % 2 ^ 1)) + c(y))) + '\n'
    else:
        res += str((c(n ** 2) + (f(x) * n - c(n) * (x % 2 ^ 1)) + c(y))) + '\n'
print(res, end='')
