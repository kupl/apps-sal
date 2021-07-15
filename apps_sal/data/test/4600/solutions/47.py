n,m = map(int,input().split())
AC = [0]*n
WA = [0]*n
ans = 0
for i in range(m):
    p,s = input().split()
    p = int(p)-1
    if s == "AC" and AC[p] == 0:
        AC[p] = 1
        ans += WA[p]
    WA[p] += 1
print(sum(AC),ans)
