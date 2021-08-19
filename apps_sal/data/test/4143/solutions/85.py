import math
n = int(input())
a = []
# r=0
a.append(math.ceil(n / int(input())))
a.append(math.ceil(n / int(input())))
a.append(math.ceil(n / int(input())))
a.append(math.ceil(n / int(input())))
a.append(math.ceil(n / int(input())))

print(max(a) + 5 - 1)
