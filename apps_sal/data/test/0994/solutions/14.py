N,M = list(map(int,input().split()))
H = []
for i in range(M):
    d,h = list(map(int,input().split()))
    H.append((d,h))
#print(H[0])
best = (H[0][0]-1) + H[0][1]
for i in range(M - 1):
    diffd = H[i + 1][0] - H[i][0]
    diffh = abs(H[i + 1][1] - H[i][1])
    if (diffd >= diffh):
        best = max(best,max(H[i + 1][1],H[i][1]) + ((diffd - diffh) // 2))
    else:
        print("IMPOSSIBLE")
        break
else:
    best = max(best,H[M - 1][1] + (N - H[M - 1][0]))
    print(best)
