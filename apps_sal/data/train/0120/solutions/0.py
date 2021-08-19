import sys
input = sys.stdin.readline
t = int(input())


def calc(x):
    return x * (x + 1) // 2


for test in range(t):
    (n, m) = list(map(int, input().split()))
    ANS = calc(n)
    k = n - m
    (q, mod) = divmod(k, m + 1)
    ANS -= calc(q + 1) * mod + calc(q) * (m + 1 - mod)
    print(ANS)
