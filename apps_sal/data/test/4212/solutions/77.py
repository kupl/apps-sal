from itertools import combinations_with_replacement as cwr
[N, M, Q] = [int(i) for i in input().split()]
req = [list(map(int, input().split())) for _ in range(Q)]
ans = 0
for seq in cwr(range(1, M + 1), N):
    sco = 0
    for i in range(Q):
        if seq[req[i][1] - 1] - seq[req[i][0] - 1] == req[i][2]:
            sco += req[i][3]
    s = max(ans, sco)
    ans = s
print(ans)
