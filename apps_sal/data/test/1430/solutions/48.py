from itertools import groupby
import sys

N, K = list(map(int, input().split()))
S = input()

S = [[i, len(list(j))] for i, j in groupby(S)]

if len(S) // 2 <= K:
    if len(S) % 2 == 1 and S[-1][0] == "0":
        if len(S) == 1:
            print((sum([j for i, j in S])))
            return

    else:
        print((sum([j for i, j in S])))
        return

ans = 0
cnt = 0
lidx = -1
for i, j in S:
    lidx += 1
    if cnt == K and i == "0":
        break
    ans += j
    if i == "0":
        cnt += 1
sidx = 0
mans = ans
for i in range(lidx, len(S)):
    ans += S[i][1]
    if i == len(S) - 1 or S[i][0] == "1":
        while True:
            ans -= S[sidx][1]
            sidx += 1
            if S[sidx][0] == "1":
                break
        mans = max(mans, ans)

print(mans)
