n,m = map(int,input().split())
a = list(map(int,input().split()))
l = [list(map(int,input().split())) for i in range(m)]
l = list(sorted(l,reverse=True,key=lambda x: x[1]))
b,c = [list(i) for i in zip(*l)]
d = [0] * n
x = min(n,sum(b))
y = 0
while x > 0:
    x -= 1
    d[x] = c[y]
    b[y] -= 1
    if b[y] == 0:
        y += 1
x = a + d
x.sort(reverse=True)
print(sum(x[:n]))
