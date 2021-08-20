import sys
input = sys.stdin.readline
N = int(input())
T = input()[:-1]
S = ['110'] * N
S = ''.join(S)
ans = 0
if S[:N] == T:
    ans += (3 * 10 ** 10 - N) // 3 + 1
if S[1:1 + N] == T:
    ans += (3 * 10 ** 10 - 1 - N) // 3 + 1
if S[2:2 + N] == T:
    ans += (3 * 10 ** 10 - 2 - N) // 3 + 1
print(ans)
