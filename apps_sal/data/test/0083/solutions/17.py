import math
n = int(input())
a = [int(x) for x in input().split()]
co1 = co2 = co3 = 0
for item in a:
    if item > 0:
        co1 += 1
    elif item < 0:
        co2 += 1
    else:
        co3 += 1
if co1 >= math.ceil(n / 2):
    print(1)
elif co2 >= math.ceil(n / 2):
    print(-1)
else:
    print(0)
