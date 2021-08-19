(n, m, r) = map(int, input().split())
books = [[int(i) for i in input().split()] for _ in range(n)]
t = []
for x in range(2 ** n):
    p = [0] * (m + 1)
    for y in range(n):
        if x >> y & 1:
            p = [a + b for (a, b) in zip(books[y], p)]
    t.append(p)
ans = []
c = True
for z in t:
    c = True
    for s in range(1, m + 1):
        if z[s] < r:
            c = False
    if c:
        ans.append(z[0])
if ans != []:
    print(min(ans))
else:
    print(-1)
