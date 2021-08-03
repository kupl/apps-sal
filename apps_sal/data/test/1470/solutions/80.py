import math
x = int(input())
a = x // 11
ama = x % 11
if ama == 0:
    print((a * 2))
elif ama <= 6:
    print((a * 2 + 1))
else:
    print((a * 2 + 2))
