import math
num_list = list(map(int, input().split()))
a = num_list[0]
b = num_list[1]
c = num_list[2]
d = num_list[3]
result = max(max(a * c, a * d), max(b * c, b * d))
print(result)
