import sys


def input():
    return sys.stdin.readline()[:-1]


t = int(input())
for _ in range(t):
    (a, b, q) = list(map(int, input().split()))
    ans = [0 for _ in range(q)]
    res = [0 for _ in range(a * b)]
    for i in range(1, a * b):
        if i % a % b != i % b % a:
            res[i] = res[i - 1] + 1
        else:
            res[i] = res[i - 1]

    def func(x):
        (quo, mod) = (x // (a * b), x % (a * b))
        return quo * res[-1] + res[mod]
    for i in range(q):
        (l, r) = list(map(int, input().split()))
        ans[i] = func(r) - func(l - 1)
    print(*ans)
