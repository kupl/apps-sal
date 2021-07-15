N,C = map(int,input().split())
T = [[0 for i in range(10**5+1)] for j in range(C)]

for i in range(N):
    s,t,c = map(int,input().split())
    T[c-1][s] += 1
    T[c-1][t] -= 1
for i in range(C):
    for j in range(10**5):
        T[i][j+1] += T[i][j]

ans = 0
for i in range(1,10**5+1):
    a = 0
    for j in range(C):
        if T[j][i] or T[j][i-1]:
            a += 1
    ans = max(ans,a)
print(ans)
