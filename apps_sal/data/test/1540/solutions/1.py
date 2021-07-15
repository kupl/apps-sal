n, m, k = map(int, input().split())
a = [set() for i in range(m)]
b = [0 for i in range(n)] 
d = [0 for i in range(m)]
for i in range(n):
    s = list(map(int, input().split()))
    for j in range(m):
        if s[j]:
            a[j].add(i)
for i in range(k):
    x, y = map(int, input().split())
    d[y - 1] += 1
    b[x - 1] -= 1
for i in range(m):
    if d[i]:
        for elem in a[i]:
            b[elem] += d[i]        
for i in range(n):
    print(b[i], end = ' ')
