def rawInput():
    return [int(x) for x in input().split()] 

n, b = rawInput()
x = rawInput()
y = rawInput()

def compute(a, b):
    dis = abs(1 - a) + abs(1 - b)
    dis = min(dis, abs(1 - a) + abs(n - b))
    dis = min(dis, abs(n - a) + abs(n - b))
    dis = min(dis, abs(n - a) + abs(1 - b))
    return dis

rlt = 0
for i in range(b):
    rlt = rlt + compute(x[i], y[i])

print(rlt)

