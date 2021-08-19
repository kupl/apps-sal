from collections import *
N = int(input())
S = input()
c = Counter(S)
ans = c['R'] * c['G'] * c['B']
for i in range(1, N // 2 + 1):
    for j in range(i, N - i):
        if S[j - i] != S[j] and S[j] != S[j + i] and (S[j + i] != S[j - i]):
            ans -= 1
print(ans)
