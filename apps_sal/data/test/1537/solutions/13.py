import sys
input = lambda: sys.stdin.readline().strip()
 
n, k = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.append(list(input()))
extra = 0
res = []
for i in range(n-k+1):
    res.append([])
    for j in range(n-k+1):
        res[-1].append(0)
 
# ROWS
 
l = {}
r = {}
for i in range(n):
    for j in range(n):
        if arr[i][j]=='B': l[i] = j; break
    for j in range(n-1, -1, -1):
        if arr[i][j]=='B': r[i] = j; break
    else: l[i] = None; r[i] = None; extra+=1
for j in range(n-k+1):
    tmp = 0
    for i in range(k):
        if l[i] is not None and l[i]>=j and r[i]<=j+k-1:
            res[0][j]+=1
            tmp+=1
    for i in range(1, n-k+1):
        res[i][j]+=tmp
        if l[i-1] is not None and l[i-1]>=j and r[i-1]<=j+k-1:
            res[i][j]-=1
            tmp-=1
        if l[i+k-1] is not None and l[i+k-1]>=j and r[i+k-1]<=j+k-1:
            res[i][j]+=1
            tmp+=1
 
# COLUMNS
 
l = {}
r = {}
for j in range(n):
    for i in range(n):
        if arr[i][j]=='B': l[j] = i; break
    for i in range(n-1, -1, -1):
        if arr[i][j]=='B': r[j] = i; break
    else: l[j] = None; r[j] = None; extra+=1
for i in range(n-k+1):
    tmp = 0
    for j in range(k):
        if l[j] is not None and l[j]>=i and r[j]<=i+k-1:
            res[i][0]+=1
            tmp+=1
    for j in range(1, n-k+1):
        res[i][j]+=tmp
        if l[j-1] is not None and l[j-1]>=i and r[j-1]<=i+k-1:
            res[i][j]-=1
            tmp-=1
        if l[j+k-1] is not None and l[j+k-1]>=i and r[j+k-1]<=i+k-1:
            res[i][j]+=1
            tmp+=1
 
print(max(max(i) for i in res)+extra)

