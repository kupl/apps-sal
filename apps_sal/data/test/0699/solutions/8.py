do_cf = False
import math
a,b,c=list(map(int,input().split(' ')))
x = math.floor(c/b)
dead = x * b
deaded = b*math.ceil(a/b)
strx = ''
for i in range(deaded, dead+1, b):
    if i-a>0:
        do_cf= True
        strx += ' ' + str(i-a)
if do_cf:
    print(strx)
else:
    print("-1")
