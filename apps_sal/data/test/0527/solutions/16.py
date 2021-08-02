from bisect import bisect_left


S = input()
T = input()
if any(c not in S for c in T):
    print((-1))
    return

N = len(S)
pos = {c: [] for c in "abcdefghijklmnopqrstuvwxyz"}
for i in range(N):
    pos[S[i]].append(i)

loop = 0
cur = 0
for c in T:
    nxt = bisect_left(pos[c], cur)
    if nxt == len(pos[c]):
        loop += 1
        cur = pos[c][0] + 1
    else:
        cur = pos[c][nxt] + 1
print((loop * N + cur))
