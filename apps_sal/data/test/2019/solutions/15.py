import math
for _ in range(int(input())):
    a = list(input())
    c1 = a.count('0')
    c2 = a.count('1')
    if min(c1,c2)%2==1:
        print('DA')
    else:
        print('NET')
