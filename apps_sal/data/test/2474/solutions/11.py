import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10 ** 9))


def write(x):
    return sys.stdout.write(x + '\n')


n = int(input())
a = list(map(int, input().split()))
M = 10 ** 9 + 7
pp = [None] * n
v = 1
for i in range(n):
    pp[i] = v
    v *= 2
    v %= M
a.sort()
a = a[::-1]
ans = 0
ans += a[0] * pow(2, 0, M) * pow(2, n - 1, M)
for i in range(1, n):
    num = a[i]
    ans += num * (pp[i] + i * pp[i - 1]) * pp[n - i - 1]
    ans %= M
ans *= pow(2, n, M)
ans %= M
print(ans)
