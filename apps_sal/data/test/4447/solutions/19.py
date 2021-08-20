(n, m) = list(map(int, input().split()))
a = list(map(int, input().split()))
s = [[] for _ in range(m)]
for i in range(n):
    s[a[i] % m].append(i)
f = []
c = 0
for _ in range(2):
    for i in range(m):
        while len(s[i]) > n // m:
            f.append((s[i].pop(), i))
        while len(s[i]) < n // m and f:
            (v, p) = f.pop()
            s[i].append(v)
            if i > p:
                d = i - p
            else:
                d = i + m - p
            a[v] += d
            c += d
print(c)
print(*a)
