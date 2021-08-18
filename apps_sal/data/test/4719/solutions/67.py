n = int(input())
d = {}
for i in range(n):
    s = input()
    d[i] = {}
    for c in s:
        if c in d[i]:
            d[i][c] += 1
        else:
            d[i][c] = 1
k = {chr(i)for i in range(97, 123)}
for e in d:
    k &= set(d[e].keys())
for t in sorted(k):
    m = float('inf')
    for e in d:
        m = min(m, d[e][t])
    print(t * m, end='')
print('')
