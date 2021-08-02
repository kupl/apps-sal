N, K = map(int, input().split())
cnt = 0
P = []
for i in range(N):
    a, b = map(int, input().split())
    P.append((a, b))

P = sorted(P)
for i in range(N):
    cnt += P[i][1]
    if cnt >= K:
        print(P[i][0])
        break
