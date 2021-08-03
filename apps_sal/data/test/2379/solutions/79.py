N, K, C = map(int, input().split())
S = input()


def get_positions():
    res = []
    i = 0
    while i < N and len(res) < K:
        if S[i] == "o":
            res.append(i)
            i = i + C + 1
        else:
            i += 1
    return res


l = get_positions()
S = S[::-1]
r = get_positions()
for i in range(K):
    r[i] = N - 1 - r[i]
S = S[::-1]

lastl = [-1] * (N + 1)
for i in range(K):
    lastl[l[i] + 1] = i
for i in range(N):
    if lastl[i + 1] == -1:
        lastl[i + 1] = lastl[i]

lastr = [-1] * (N + 1)
for i in range(K):
    lastr[r[i]] = i
for i in range(N - 1, -1, -1):
    if lastr[i] == -1:
        lastr[i] = lastr[i + 1]

for i in range(N):
    if S[i] == "x":
        continue
    li = lastl[i]
    ri = lastr[i + 1]
    cnt = 0
    if li != -1:
        cnt += (li + 1)
    if ri != -1:
        cnt += (ri + 1)
    if li != -1 and ri != -1 and r[ri] - l[li] <= C:
        cnt -= 1

    if cnt >= K:
        continue
    print(i + 1)
