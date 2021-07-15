N = int(input())
P = list(map(lambda x: int(x) - 1, input().split()))

D = [0] * N

for i in range(N):
    D[P[i]] = i

lt = 0
used = [0] * N
res = []

for i in range(N):
    if used[i]:
        continue
    if lt > D[i]:
        print(-1)
        break
    rt = D[i]
    for j in range(lt, rt)[::-1]:
        D[P[j]], D[P[j + 1]] = D[P[j + 1]], D[P[j]]
        P[j], P[j + 1] = P[j + 1], P[j]
        res.append(j + 1)
    for j in range(lt, rt):
        used[j] = 1
    lt = rt
else:
    for i in range(N):
        if P[i] != i:
            print(-1)
            break
    else:
        print('\n'.join(map(str, res)))
