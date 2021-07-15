#https://atcoder.jp/contests/abc150/tasks/abc150_c

from itertools import permutations

b= int(input())
c= []

d= list(map(int, input().split()))
e= list(map(int, input().split()))

for a in range(1, b+1):
    c.append(a)

c= list(map(str, range(1, b+1)))

#print(c)
d= ''.join(map(str, d))
e= ''.join(map(str, e))

f= list(map(''.join, permutations(c, b)))
#print(f)

D= f.index(d)
E= f.index(e)
if(D>E):
    print(D-E)
else:
    print(E-D)
