from sys import stdin,stdout
input = stdin.readline

b = {}
s = {}

n, l = map(int,input().split(' '))
for i in range(n):
    d,p,q = input().split(' ')
    p,q = int(p),int(q)
    if d == 'B':
        try:
            b[p] += q
        except KeyError:
            b[p] = q
    else:
        try:
            s[p] += q
        except KeyError:
            s[p] = q

for key in sorted(sorted(s)[0:min(l,len(s))],reverse=True):
    print("S %s %s" % (key, s[key]))

for key in sorted(b,reverse=True)[0:min(l,len(b))]:
    print("B %s %s" % (key, b[key]))
