import sys
sys.setrecursionlimit(100100)
S = input()
N = len(S)
table = [-1 for i in range(N)]


def dp(n):
    if S[n] == 'R' and S[n + 1] == 'L':
        return n
    if S[n] == 'L' and S[n - 1] == 'R':
        return n
    if table[n] > -1:
        return table[n]
    if S[n] == 'R':
        if S[dp(n + 1)] == 'R':
            table[n] = dp(n + 1) + 1
        else:
            table[n] = dp(n + 1) - 1
    elif S[dp(n - 1)] == 'R':
        table[n] = dp(n - 1) + 1
    else:
        table[n] = dp(n - 1) - 1
    return table[n]


list = [0 for i in range(N)]
for i in range(N):
    list[dp(i)] += 1
for ans in list:
    print(ans, end=' ')
print()
