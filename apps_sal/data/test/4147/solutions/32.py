from itertools import product
(N, A, B, C) = map(int, input().split())
abc = [C, B, A]
lst = [int(input()) for _ in range(N)]
ans = []
for l in product([0, 1, 2, 3], repeat=N):
    cnt = [[], [], [], []]
    for (i, ll) in enumerate(l):
        cnt[ll].append(lst[i])
    mp = 0
    p = []
    for i in cnt[:3]:
        if len(i) != 0:
            mp += (len(i) - 1) * 10
        p.append(sum(i))
    p.sort()
    if p[0] != 0:
        for i in range(3):
            mp += abs(p[i] - abc[i])
        ans.append(mp)
print(min(ans))
