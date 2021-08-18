n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(-1)
    return

x = min(a)
t = a.index(x)
d = []
c = []
for i in range(n):
    if i != t:
        d.append(i)
        c.append(a[i])
if sum(c) == x:
    print(-1)
else:
    print(1)
    print(t + 1)
