from itertools import product
(N, M) = list(map(int, input().split()))
k = []
S = []
for _ in range(M):
    ks = list(map(int, input().split()))
    k.append(ks[0])
    S.append(ks[1:])
p = list(map(int, input().split()))
onoff = list(product([0, 1], repeat=N))
ans = 0
for i in onoff:
    cnt = 0
    for (ind, s) in enumerate(S):
        state = 0
        for o in s:
            state += i[o - 1]
        if state % 2 == p[ind]:
            cnt += 1
    if cnt == M:
        ans += 1
print(ans)
