(n, m) = map(int, input().split())
a = list(map(int, input().split()))
q = []
for i in range(n):
    q.append(a[i])
q.sort()
q = q[-m:]
s = 0
for i in range(m):
    s += q[i]
print(s)
s = 1
w = []
f = 1
for i in range(n):
    if a[0] in q:
        w.append(s)
        f += s
        s = 0
        q.remove(a[0])
    a.remove(a[0])
    s += 1
w[-1] += n - f + 1
for i in range(m):
    print(w[i], end=' ')
