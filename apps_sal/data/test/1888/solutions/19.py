(n, m) = list(map(int, input().split()))
l = [0 for i in range(n + 3)]
for i in range(m):
    (x, y, c) = list(map(int, input().split()))
    l[x] += c
    l[y] -= c
s = 0
for i in l:
    s += max(i, 0)
print(s)
