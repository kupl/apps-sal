N = int(input())

AB = []

for _ in range(N):
    AB.append(list(map(int, input().split())))

A_idx = [(AB[i][0], i) for i in range(N)]
B_idx = [(AB[i][1], i) for i in range(N)]

A_idx.sort(key=lambda e:e[0])
B_idx.sort(key=lambda e:e[0])

if N % 2 == 1:
    diff = B_idx[N//2][0]-A_idx[N//2][0]
    print(diff+1)
else:
    l = N//2-1
    u = N//2
    diff = (B_idx[l][0]+B_idx[u][0])-(A_idx[l][0]+A_idx[u][0])
    print(diff+1)
