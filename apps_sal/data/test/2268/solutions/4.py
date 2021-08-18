import sys


n, m = [int(x) for x in input().split()]
s = input()
c1 = ord('a')
c2 = ord('z')
ma = [i for i in range(c2 - c1 + 1)]
where = [i for i in range(c2 - c1 + 1)]
for i in range(m):
    cf, cs = [ord(c) for c in input().split()]
    wcf = where[cf - c1]
    wcs = where[cs - c1]
    ma[wcf], ma[wcs] = ma[wcs], ma[wcf]
    where[cf - c1], where[cs - c1] = where[cs - c1], where[cf - c1]

ans = []
for c in s:
    cur = ord(c)
    ans.append(chr(ma[cur - c1] + c1))

print(''.join(ans))
