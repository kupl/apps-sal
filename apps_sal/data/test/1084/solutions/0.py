(n, m) = list(map(int, input().split()))
a = [-1] * m
b = []
f = True
for i in range(n):
    s = input()
    q = set()
    for j in range(len(s)):
        if s[j] == '#':
            q.add(j)
    for j in range(len(s)):
        if s[j] == '#':
            if a[j] == -1:
                a[j] = i
            elif b[a[j]] != q:
                f = False
    b.append(q)
if f:
    print('Yes')
else:
    print('No')
