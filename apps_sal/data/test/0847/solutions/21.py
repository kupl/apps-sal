import math
(n, k) = input().split(' ')
s = math.fabs(sum([int(x) for x in input().split(' ')]))
print(int(math.ceil(s / int(k))))
