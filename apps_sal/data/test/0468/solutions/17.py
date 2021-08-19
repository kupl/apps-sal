import math
inp = input().split(' ')
x = int(inp[0])
y = int(inp[1])
res1 = y * math.log(1.0 * x)
res2 = x * math.log(1.0 * y)
if res1 == res2:
    print('=')
elif res1 > res2:
    print('>')
else:
    print('<')
