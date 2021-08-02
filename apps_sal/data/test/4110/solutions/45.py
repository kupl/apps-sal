import math

D, G = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(D)]

ans = float("inf")

for bit in range(1 << D):
    cnt = 0
    sum = 0
    pids = set(range(D))

    for i in range(D):
        if bit & (1 << i):
            sum += pc[i][0] * (i + 1) * 100 + pc[i][1]
            cnt += pc[i][0]
            pids.discard(i)

    if sum < G:
        pid = max(pids)
        n = min(pc[pid][0], math.ceil((G - sum) / ((pid + 1) * 100)))
        cnt += n
        sum += n * (pid + 1) * 100

    if sum >= G:
        ans = min(ans, cnt)

print(ans)
