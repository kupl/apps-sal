N = int(input())
L = [[int(l) for l in input().split()] for _ in range(N)]

L1 = [0]*N
L2 = [0]*N
for i in range(N):
    L1[i] = L[i][0]+L[i][1]
    L2[i] = L[i][0]-L[i][1]

L1.sort()
L2.sort()
print(max(L1[-1]-L1[0], L2[-1]-L2[0]))
