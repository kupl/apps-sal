(n, m) = map(int, input().split())
s = set(range(1, n + 1))
for i in range(m):
    for j in map(int, input().split()):
        if j in s:
            s.remove(j)
c = s.pop()
print(n - 1)
for i in range(1, n + 1):
    if i != c:
        print(c, i)
