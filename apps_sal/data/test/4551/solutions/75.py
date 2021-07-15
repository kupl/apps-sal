a,b,c,d=(int(x) for x in input().split())
e = int(a) + int(b)
f = int(c) + int(d)
if e > f:
    print('Left')
elif e < f:
    print('Right')
else:
    print('Balanced')
