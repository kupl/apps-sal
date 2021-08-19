import bisect
S = input()
T = input()
D = dict()
for i in range(len(T)):
    if T[i] in D:
        continue
    else:
        D[T[i]] = []
for i in range(len(S)):
    if S[i] in D:
        D[S[i]].append(i)
if len(set(T) - set(S)) > 0:
    print(-1)
else:
    r = -1
    cnt = 0
    for i in range(len(T)):
        m = bisect.bisect_right(D[T[i]], r)
        if m < len(D[T[i]]):
            r = D[T[i]][m]
        else:
            r = D[T[i]][0]
            cnt += 1
    print(len(S) * cnt + r + 1)
