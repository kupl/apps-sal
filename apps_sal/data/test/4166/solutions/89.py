N,M = map(int,input().split())
a = [-1]*N
ans = 0
for i in range(M):
    s,c = map(int,input().split())
    if a[s-1] == -1:
        a[s-1] = c
    elif a[s-1] != c:
        ans = -1
        break
if a[0] == 0 and N>1:
    ans = -1
if ans != -1:
    if a[0] == -1 and N>1:
        a[0] = 1
    if a[0] == -1 and N == 1:
        a[0] = 0
    for i in range(N):
        if a[i] == -1:
            a[i] = 0
        a[i] = str(a[i])
    ans = "".join(a)
print(ans)
