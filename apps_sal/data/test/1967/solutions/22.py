ar1 = []
(n, m) = map(int, input().split())
ar = []
for i in range(m):
    s1 = []
    s = input().rstrip()
    for j in range(n):
        s1.append(s[j])
    ar.append(s1)
ark = []
for i in range(m):
    ark.append(ar[m - i - 1])
ar = ark[:]
for i in range(n):
    s = []
    for j in range(m - 1, -1, -1):
        s.append(ar[j][i])
    ar1.append(s)
for i in range(n):
    for j in ar1[i]:
        print(j * 2, end='')
    print()
    for j in ar1[i]:
        print(j * 2, end='')
    print()
