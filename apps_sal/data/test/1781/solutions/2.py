from collections import Counter
n, k = list(map(int, input().split()))
a = set()
c = [set() for i in range(3)]
b = set()
z = 0
for i in range(n):
    s = input()
    for i0 in range(len(s)):
        if s[i0] == '.':
            a.add(tuple([i, i0]))
        elif s[i0] == 'S':
            b.add(tuple([i, i0]))
    for i0 in range(len(s)):
        if s[i0] == '.':
            zz = 0
            if tuple([i, i0 + 1]) in b:
                zz = zz + 1
            if tuple([i, i0 - 1]) in b:
                zz = zz + 1
            c[zz].add(tuple([i, i0]))
c = list(c[0]) + list(c[1]) + list(c[2])
for i in range(k):
    a.remove(c[i])
for i in b:
    if (i[1] != 2) and (i[1] != 7) and (i[1] != 11):
        if not(tuple([i[0], i[1] + 1]) in a):
            z = z + 1
    if (i[1] != 4) and (i[1] != 9) and (i[1] != 0):
        if not(tuple([i[0], i[1] - 1]) in a):
            z = z + 1
c = set(c)

print(z)
for i in range(n):
    s = ''
    for i0 in range(12):
        if i0 == 3 or i0 == 8:
            s = s + '-'
        elif tuple([i, i0]) in a:
            s = s + '.'
        elif tuple([i, i0]) in b:
            s = s + 'S'
        elif tuple([i, i0]) in c:
            s = s + 'x'
        else:
            s = s + 'P'
    print(s)
