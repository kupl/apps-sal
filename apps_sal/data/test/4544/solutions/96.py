N, *A = map(int, open(0).read().split())

C = {}
for a in A:
    if a in C.keys():
        C[a] += 1
    else:
        C[a] = 1
B = list(C.items())
B.sort(key=lambda x: x[0])

M = len(B)
ans = 0
for i in range(M):
    count = B[i][1]
    if i-1 >= 0 and B[i-1][0] == B[i][0]-1:
        count += B[i-1][1]
    if i+1 < M and B[i+1][0] == B[i][0]+1:
        count += B[i+1][1]
    ans = max(ans, count)
print(ans)
