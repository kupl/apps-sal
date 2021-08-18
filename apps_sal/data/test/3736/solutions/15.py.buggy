from sys import stdin

__author__ = 'artyom'

exclusions = 'BCDEFGJKLNPQRSZ'
st = stdin.readline().strip()
l = len(st)
p = l // 2
for i in range(l):
    if st[i] in exclusions or (i <= p and st[i] != st[l - i - 1]):
        print('NO')
        return

print('YES')
