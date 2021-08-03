N, M = map(int, input().split())
K = []
S = []
for i in range(M):
    k = 0
    s = []
    k, *s = map(int, input().split())
    K.append(k)
    S.append(s)
P = list(map(int, input().split()))
res = 0
for bit in range(1 << N):
    judge = True
    for i in range(M):
        cnt = 0
        for s in S[i]:
            cnt += (bit >> s - 1) & 1
        if cnt % 2 != P[i]:
            judge = False
            break
    if judge:
        res += 1
print(res)
