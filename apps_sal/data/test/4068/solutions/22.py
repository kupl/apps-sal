N,M = map(int,input().split())
lsS = [1,1]+[0]*(N-1)
for i in range(M):
    lsS[int(input())] = -1
for i in range(2,N+1):
    if lsS[i] == -1:
        continue
    else:
        if lsS[i-2] != -1:
            lsS[i] += lsS[i-2]
        if lsS[i-1] != -1:
            lsS[i] += lsS[i-1]
        lsS[i] = lsS[i]%(10**9+7)
print(lsS[N])
