
from sys import stdin, stdout

R = lambda: map(int, input().split())
S = list(stdin.readline().strip())
Q = int(input())
n = len(S)
S = list(S)
sum_array = [[0] * (n + 1) for _ in range(26)]


def lowbit(x):
    return x & -x


def add(x, val, idx):
    while x <= n:
        sum_array[idx][x] += val
        x += lowbit(x)


def sum(x, idx):
    res = 0
    while x > 0:
        res += sum_array[idx][x]
        x -= lowbit(x)
    return res


for i in range(n):
    idx = ord(S[i]) - 97
    add(i + 1, 1, idx)

for _ in range(Q):
    A = stdin.readline().split()
    a, b, c = int(A[0]), int(A[1]), A[2]
    if a == 1:
        pre = ord(S[b - 1]) - 97
        cur = ord(c) - 97
        S[b - 1] = c
        add(b, -1, pre)
        add(b, 1, cur)
    else:
        c = int(c)
        if c - b == 0:
            print(1)
        else:
            res = 0
            for i in range(26):
                diff = sum(c, i) - sum(b - 1, i)
                res += int(diff > 0)
            print(res)
