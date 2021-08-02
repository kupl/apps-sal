import sys
readline = sys.stdin.readline

T = int(readline())
Ans = [None] * T
for qu in range(T):
    S = list(map(int, readline().strip()))
    N = len(S)
    so = S.count(1)
    ans = min(so, N - so)

    table = S[:]
    for i in range(1, N):
        table[i] += table[i - 1]

    for i in range(N):
        one = table[i]
        zero = i + 1 - one

        no = so - one
        nz = N - (i + 1) - no

        ans = min(ans, no + zero, one + nz)
    Ans[qu] = ans

print('\n'.join(map(str, Ans)))
