import math
(m, d) = list(map(int, input().split()))
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = days[m - 1]
print(math.ceil((day + d - 1) / 7))
