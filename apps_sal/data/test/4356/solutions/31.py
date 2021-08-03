N, M = map(int, input().split())
Als = []
Bls = []
ans = 'No'
if Bls == Als:
    ans = 'Yes'
for i in range(N):
    Als.append(input())
for i in range(M):
    Bls.append(input())
for i in range(N - M):
    for j in range(0, N - M):
        for k in range(M):
            if Bls[k] == Als[i + k][j:M + j]:
                ans = 'Yes'
            else:
                ans = 'No'
                break
        if ans == 'Yes':
            break
    if ans == 'Yes':
        break
print(ans)
