n = int(input())
res = []
x = set()
y = set()
for i in range(n*n):
    a,b = map(int,input().split())
    if not (a in x or b in y):
        x.add(a)
        y.add(b)
        res.append(i+1)
print(*res)
