import math
n = int(input())

l = list(map(int, input().split(" ")))
li = []
for i in l:
    if(i > 0):
        li.append(i)
s = sum(li)
found = False
if(s%2 == 0):
    m = 10000
    for i in li:
        if i < m and i%2==1:
            m = i
            found = True
    if(found):    
        m2 = -10000
        for i in l:
            if i > m2 and i < 0 and i%2 == 1:
                m2 = i
        if(abs(m2) > m):
            print(s-m)
        else:
            print(s+m2)
    else:
        m2 = -10000
        for i in l:
            if i > m2 and i < 0 and i%2 == 1:
                m2 = i
        print(s+m2)
else:
    print(s)
    
    
        

