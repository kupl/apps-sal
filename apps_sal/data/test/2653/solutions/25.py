n, q = map(int, input().split())
e = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    e[a].append(b)
    e[b].append(a)
ps = [0 for i in range(n)]
for i in range(q):
    p, x = map(int, input().split())
    ps[p - 1] += x

s = [-1 for i in range(n)]
sc = [0]
s[0] = 0
while sc:
    nsc = []
    for i in sc:
        s[i] += ps[i]
        for j in e[i]:
            if s[j] == -1:
                nsc.append(j)
                s[j] = s[i]
    sc = nsc

r = ""
for i in range(n):
    r += str(s[i]) + " "
print(r[:-1])
