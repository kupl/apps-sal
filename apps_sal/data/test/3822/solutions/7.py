import sys
import math
data = sys.stdin.read()
data = data.split(' ')
n = int(data[0])
l = int(data[1])
w = int(data[2])
v = int(data[3])
k = int(data[4])
z = math.ceil(n / k)
top = l / w - l / (2 * w * z) + l / (2 * v * z)
bot = 1 + v / (2 * w * z) - 1 / (2 * z)
print(top / bot)
