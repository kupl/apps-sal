import math
line = input()

integers = [int(i) for i in line.split()]
n = integers[0]
k = integers[1]

for i in range(n):
    if(n - i - 2 != -1):
        print((str(0) + ' ')*i + str(k) + ' ' + (str(0) + ' ')*(n - i - 2) + str(0))
    else:
        print((str(0) + ' ')*i + str(k))

