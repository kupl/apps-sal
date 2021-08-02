n, m = map(int, input().split())
d = {}
for j in range(n):
    c, con = input().split()
    d[c] = con
v = {}
for j in range(m):
    c = input()
    if c in v:
        v[c] += 1
    else:
        v[c] = 1
cv = {}
w = 0
for j in v:
    if d[j] in cv:
        cv[d[j]] += v[j]
    else:
        cv[d[j]] = v[j]
    if cv[d[j]] > w:
        w = cv[d[j]]
        wc = d[j]
    elif cv[d[j]] == w:
        if d[j] < wc:
            wc = d[j]
print(wc)
wv = 0
for j in v:
    if v[j] > wv:
        wv = v[j]
        wc = j
    elif v[j] == wv:
        if j < wc:
            wc = j
print(wc)
