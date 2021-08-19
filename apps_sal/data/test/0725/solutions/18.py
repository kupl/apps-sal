(N, M) = list(map(int, input().split()))
mat = []
for i in range(N):
    mat.append(input().split())
wgb = 'WGB'
flg = False
for i in range(N):
    for j in range(M):
        if mat[i][j] not in wgb:
            flg = True
            break
    if flg:
        break
if flg:
    print('#Color')
else:
    print('#Black&White')
