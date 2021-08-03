import sys


def I():
    return sys.stdin.readline().rstrip()


n, c = list(map(int, I().split()))
a = list(map(int, I().split()))
b = list(map(int, I().split()))

e = [0] + [1003 * n] * (n - 1)
s = [0] + [1003 * n] * (n - 1)

for i in range(0, n - 1):
    e[i + 1] = min(c + s[i] + b[i], e[i] + b[i])
    s[i + 1] = min(s[i], e[i]) + a[i]
    if i == 0:
        e[i + 1] += c

ans = [min(i, j) for i, j in zip(e, s)]
print(*ans)
