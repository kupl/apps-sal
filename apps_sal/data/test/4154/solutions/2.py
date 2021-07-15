N, M = map(int, input().split())

L = []

for i in range(M):
    LR = list(map(int, input().split()))
    L.append(LR)

res = [L[0][0], L[0][1]]

for i in range(M):
    res = [max(res[0], L[i][0]), min(res[1], L[i][1])]

if res[1] < res[0]:
    print(0)
else: 
    print(res[1] - res[0] + 1)
