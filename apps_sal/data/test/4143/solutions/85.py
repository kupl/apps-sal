import math
n = int(input())
a = []
a.append(math.ceil(n / int(input())))
a.append(math.ceil(n / int(input())))
a.append(math.ceil(n / int(input())))
a.append(math.ceil(n / int(input())))
a.append(math.ceil(n / int(input())))
print(max(a) + 5 - 1)
