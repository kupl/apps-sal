n = int(input())
l = []
r = []
for _ in range(n):
    x, y = map(int, input().split())
    l.append(x)
    r.append(y)
print(n+sum(map(max, sorted(l), sorted(r))))
