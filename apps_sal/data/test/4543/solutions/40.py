import math
a, b = input().split()
q = int(a + b)
if math.sqrt(q) // 1 == math.sqrt(q):
    print("Yes")
else:
    print('No')
