import time
(n, m) = (int(i) for i in input().split())
app = []
for i in range(n):
    app.append([0 for j in range(m)])
    a = [int(j) for j in input().split()]
    for j in range(len(a)):
        app[i][divmod(j, 2)[0]] += a[j]
start = time.time()
s = 0
for i in range(n):
    s += sum([1 for j in app[i] if j > 0])
print(s)
finish = time.time()
