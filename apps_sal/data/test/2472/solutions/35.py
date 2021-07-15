n = int(input())
work = [list(map(int,input().split())) for _ in range(n)]
work = sorted(work,key = lambda x:x[1])
a = [0] * n
a[0] = work[0][0]
for i in range(1,n):
    a[i] = a[i-1] + work[i][0]
ans = 'Yes'
for j in range(n):
    if a[j] > work[j][1]:
        ans = 'No'
        break
print(ans)
