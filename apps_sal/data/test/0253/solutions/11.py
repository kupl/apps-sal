import math
x1,x2,x3 = list(map(int,input().split()))
kmm = math.gcd(x1,math.gcd(x2,x3))
a =[x1,x2,x3]
a.sort()
if min(a) >= 4 :print('NO')
elif min(a) == 3:
    if max(a) == 3:print('YES')
    else:print("NO")
elif min(a) == 1:print("YES")
elif min(a) == 2:
    if a.count(2) >= 2:print("YES")
    elif a == [2,4,4]:print("YES")
    else: print("NO")

