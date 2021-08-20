(n, m) = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
b = [int(_) for _ in input().split()]
p = list(a[b[0] - 1])
for i in range(1, len(b)):
    s = a[b[i] - 1]
    if len(s) != len(p):
        print('No')
        raise SystemExit
    for j in range(len(s)):
        if s[j] != p[j] and p[j] != '?':
            p[j] = '?'
k = 0
f = False
for i in range(n):
    if k < m and i + 1 == b[k]:
        k += 1
        continue
    s = a[i]
    if len(s) == len(p):
        f = True
        for j in range(len(s)):
            if s[j] != p[j] and p[j] != '?':
                f = False
                break
    if f:
        print('No')
        raise SystemExit
print('Yes')
print(''.join(p))
