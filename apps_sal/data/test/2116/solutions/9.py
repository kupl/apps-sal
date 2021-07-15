n, m, k = map(int, input().split())
p, v = input().split(), 0
for i in range(n):
    for x in input().split():
        c = p.index(x)
        v += c + 1
        p.pop(c)
        p.insert(0, x)
print(v)
