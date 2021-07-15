N,M = map(int,input().split())
A=[input() for _ in range(N)]
B=[input() for _ in range(M)]

ans="No"

for i in range(N-M+1):
    for j in range(N-M+1):
        flag = True
        for k in range(M):
            for l in range(M):
                if A[i+k][j+l]!=B[k][l]:
                    flag = False
                    break
                    
        if flag:
            ans="Yes"
            break

print(ans)
