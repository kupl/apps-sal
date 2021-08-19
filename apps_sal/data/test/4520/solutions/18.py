(n, k) = map(int, input().split())
p = []
t = [0] * 200
for i in range(n):
    (l, r) = map(int, input().split())
    p.append((i + 1, l, r))
p.sort(key=lambda x: x[1])
r = []
opened = []
for pp in p:
    opened = list(filter(lambda x: x[2] >= pp[1], opened))
    opened.append(pp)
    if len(opened) > k:
        opened.sort(key=lambda x: x[2])
        (x, _, _) = opened.pop()
        r.append(x)
print(len(r))
print(*r)
