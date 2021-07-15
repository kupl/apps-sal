import math

out = []

for i in range(int(input())):
    x, y = map(int,input().split())
    out.append(180 * (math.atan2(y,x) / math.pi))
    
out.sort()

res = out[-1] - out[0]

for i in range(len(out)-1):
    res = min(res, 360 - out[i+1] + out[i])
    
print(res)
