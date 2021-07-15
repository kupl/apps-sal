N, M, X = [int(i) for i in input().split()]
CA = []
for i in range(N):
    CA.append([int(j) for j in input().split()])
#print(CA)
mcost = 10**10


for i in range(2**N):
    learn = [0]*M
    cost = 0
    bn = str(bin(i))[2:].zfill(N)
    #print(bn)
    for j,b in enumerate(bn):
        if b == "1":
            cost += CA[j][0]
            for m in range(M):
                learn[m] += CA[j][m+1]
                
    learn.sort()
    #print(learn)
    if learn[0] >= X:
        mcost = min(mcost, cost)

if mcost == 10**10:
    mcost = -1

print(mcost)
