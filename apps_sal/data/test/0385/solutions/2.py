n, m, p = list(map(int, input().split()))
x, v, s, l, r = [0] * n, [], input(), list(range(-1, n)), list(range(1, n + 2))
p -= 1
for i, c in enumerate(s):
    if c == '(':
        v.append(i)
    else:
        j = v.pop()
        x[i] = j
        x[j] = i
for c in input():
    if c == 'D':
        if s[p] == '(':
            p = x[p]
        q = l[x[p]]
        p = r[p]
        l[p], r[q] = q, p
        if p == n:
            p = l[p]
    else:
        p = (r if c == 'R' else l)[p]
q = p
while p != -1:
    v.append(s[p])
    p = l[p]
v.reverse()
del v[-1]
while q != n:
    v.append(s[q])
    q = r[q]
print(''.join(v))
