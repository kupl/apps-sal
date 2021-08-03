import math
inputs = [int(x) for x in input().split()]
y = inputs[0]
k = inputs[1]
n = inputs[2]
result = ''
x = k - (y % k)
i = x
while i + y <= n:
    result += str(i) + ' '
    i += k
if len(result):
    print(result[0:len(result) - 1])
else:
    print('-1')
