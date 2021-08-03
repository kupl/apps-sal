import math
n = int(input())
x = []
for i in range(5):
    x.append(int(input()))
if n == min(x):
    print(5)
else:
    print(4 + math.ceil(n / min(x)))
