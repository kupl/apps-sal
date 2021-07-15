from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      list(map(int, input().split()))
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

a,b = inm()
c = [ ['#']*50 for i in range(45) ]
c.extend([ ['.']*50 for i in range(45) ])
for z in range(a-1):
    c[(z//25)*2][(z%25)*2] = '.'
for z in range(b-1):
    c[(z//25)*2+50][(z%25)*2] = '#'
print('90 50')
for i in range(90):
    print((''.join(c[i])))

