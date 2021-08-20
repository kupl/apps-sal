import sys
readline = sys.stdin.readline


def calc(x):
    D = len(table)
    J = table[-1]
    return x // D * J + table[x % D]


Q = int(readline())
Ans = [None] * Q
for qu in range(Q):
    (A, B, T) = map(int, readline().split())
    table = [0] * (A * B)
    for i in range(1, A * B):
        if i % A % B != i % B % A:
            table[i] = 1 + table[i - 1]
        else:
            table[i] = table[i - 1]
    ans = [None] * T
    for t in range(T):
        (l, r) = map(int, readline().split())
        l -= 1
        ans[t] = calc(r) - calc(l)
    Ans[qu] = ' '.join(map(str, ans))
print('\n'.join(map(str, Ans)))
