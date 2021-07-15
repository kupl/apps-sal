n = int(input())
a = [int(x) for x in input().split()]
s,f = [int(x) for x in input().split()]
zones = f-s
currans = 1
currmax = sum(a[s-1 : f-2])
ans=1
maxppl = currmax
fst = s-1
lst = f-2
for currans in range(2, n+1):
    currmax += a[fst-1 if fst > 0 else n-1]
    currmax -= a[lst]
    fst = fst-1 if fst > 0 else n-1
    lst = lst - 1 if lst > 0 else n - 1
    if currmax > maxppl:
        maxppl = currmax
        ans = currans
print(ans)

