import sys
read = lambda t=int: list(map(t,sys.stdin.readline().split()))
array = lambda *ds: [array(*ds[1:]) for _ in range(ds[0])] if ds else 0

val = {'q':9,'r':5,'b':3,'n':3,'p':1}
s = ''.join(sys.stdin.readline() for _ in range(8))
res = 0
for c in s:
    if c.islower():
        res += val.get(c, 0)
    else:
        res -= val.get(c.lower(), 0)

if res == 0:
    print("Draw")
if res < 0:
    print("White")
if res > 0:
    print("Black")

