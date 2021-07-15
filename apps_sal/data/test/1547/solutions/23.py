n, m, k = map(int, input().split())
A = [0] * n
for i in range(n):
    A[i] = [0,0]
B = [0] * m
for i in range(m):
    B[i] = [0,0]
for i in range(k):
    per = input().split()
    if per[0] == '1':
        A[int(per[1])-1] = [int(per[2]), i+1]
    else:
        B[int(per[1])-1] = [int(per[2]), i+1]
ans = [0] * n
for i in range(n):
    ans[i] = [0] * m

for i in range(n):
    for j in range(m):
        
        if A[i][1] > B[j][1]:
            ans[i][j] = A[i][0]
        else:
            ans[i][j] = B[j][0]

for i in ans:
    print(' '.join(map(str,i)))
