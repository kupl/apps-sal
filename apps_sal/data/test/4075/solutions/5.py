from itertools import product
N, M = map(int, input().split())
switch = []
for _ in range(M):
    tmp = list(map(int, input().split()))
    switch.append(tmp[1:])
p = list(map(int, input().split()))

candidate = list(product([0, 1], repeat=N))

ans = 0
for cand in candidate:
    flag = True
    for idx, snum in enumerate(switch):
        tmp = 0
        for s in snum:
            tmp += cand[s - 1]
        if p[idx] != tmp % 2:
            flag = False
            break
    if flag:
        ans += 1
print(ans)
