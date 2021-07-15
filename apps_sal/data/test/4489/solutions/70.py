import collections

N = int(input())
S = [input() for i in range(N)]
M = int(input())
T = [input() for i in range(M)]

maxi = 0

for i in range(len(S)):
    if S.count(S[i]) - T.count(S[i]) > maxi:
        maxi = S.count(S[i]) - T.count(S[i])

print(maxi)
