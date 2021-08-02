from math import *
a, b, c, d, k = map(int, input().split())
per1 = max(a, c)
per2 = min(b, d)
if per2 >= per1:
    if per1 <= k <= per2:
        print(per2 - per1)
    else:
        print(per2 - per1 + 1)
else:
    print(0)
