from collections import *

N = int(input())
S = input()
c = Counter(S)

ans = c['R'] * c['G'] * c['B']

for i in range(N):
    for j in range(i + 1, N):
        if S[i] == S[j]:
            continue
        k = j * 2 - i
        if k >= N or S[k] == S[i] or S[k] == S[j]:
            continue
        ans -= 1

print(ans)
