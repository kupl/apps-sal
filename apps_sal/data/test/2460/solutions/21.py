n, m = list(map(int,input().split()))
x = list(map(int,input().split()))
t = list(map(int,input().split()))
arr = []
pep = {}
for i in range(n+m):
    if t[i] == 0:
        arr.append(i)
        pep[x[i]] = 0
    else:
        for j in arr:
            pep[x[j]] = i
        arr = []
for i in range(n+m-1, -1, -1):
    if t[i] == 0:
        arr.append(i)
    else:
        for j in arr:
            if abs(x[j] - x[i]) <= abs(x[pep[x[j]]] - x[j]):
                pep[x[j]] = i
        arr = []
ans = []
for i in range(n+m):
    if t[i]:
        ans.append(1)
    else:
        ans.append(0)
for i in pep:
    ans[pep[i]] += 1
for i in ans:
    if i:
        print(i-1, end = ' ')



