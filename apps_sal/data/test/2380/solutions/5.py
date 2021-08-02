N, M = map(int, input().split())

As = [0] + list(map(int, input().split()))
As.sort(reverse=True)
BCs = [(0, 0)]

memo = [0] * N

for _ in range(M):
    b, c = map(int, input().split())
    BCs.append((b, c))

BCs.sort(key=lambda x: x[1], reverse=True)

cnt = 0
rlt = 0
i = 0
j = 0
while cnt < N:
    if As[i] >= BCs[j][1]:
        rlt += As[i]
        cnt += 1
        i += 1
    else:
        if cnt + BCs[j][0] < N:
            rlt += BCs[j][0] * BCs[j][1]
            cnt += BCs[j][0]
            j += 1
        else:
            rlt += (N - cnt) * BCs[j][1]
            break

print(rlt)
