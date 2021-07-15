n, m = map(int,input().split( ))
a = list(map(int, input().split( )))
k = sum(a)
l = list()
for i in range(n):
    if a[i] >= k/(4*m):
        l.append(a[i])
if len(l)>= m:
    print("Yes")
else:
    print("No")
