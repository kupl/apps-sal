import sys
input = sys.stdin.readline
mod = 998244353
n = int(input())
S = input().strip()
ANS = 1
for s in 'abcdefghijklmnopqrstuvwxyz':
    if s == S[0] or s == S[-1]:
        for i in range(n):
            if S[i] != s:
                break
        l = i
        for i in range(n - 1, -1, -1):
            if S[i] != s:
                break
        r = i
        ANS = (ANS + (l + 1) * (n - r) - 1) % mod
print(ANS)
