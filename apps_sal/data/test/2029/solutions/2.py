n,s = map(int,input().split())
c = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int,input().split())
    c[a-1].append(b)
    c[b-1].append(a)
d = set()
k = 0
for i in range(n):
    if len(c[i]) == 1:
        d.add(i)
        if not (c[i][0] - 1) in d:
            k += 1
if n == 2:
    print(s)
else:
    print(round(s * 2 / k,7))
