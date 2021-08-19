import math
(a, b) = list(map(int, input().split()))
number = int(str(a) + str(b))
root = math.sqrt(number)
if int(root + 0.5) ** 2 == number:
    print('Yes')
else:
    print('No')
