import math
n = int(input())
b = math.floor(math.sqrt(n))
bb = b * b
if bb == n:
    print(b * 4)
else:
    left = n - bb
    if left <= b:
        print(b * 4 + 2)
    else:
        print(b * 4 + 4)
