import sys
f = sys.stdin
(n, m, k) = map(int, f.readline().strip().split())
s = f.readline().strip()
sp = [0] * m
for i in range(1, n):
    s = f.readline().strip()
    for l in range(m):
        if s[l] == 'U':
            if i % 2 == 0:
                sp[l] += 1
        elif s[l] == 'R':
            mi = l + i
            if mi < m:
                sp[mi] += 1
        elif s[l] == 'L':
            mi = l - i
            if mi >= 0:
                sp[mi] += 1
print(' '.join([str(it) for it in sp]))
