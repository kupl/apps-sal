from math import inf

def vect(x, y):
    return abs(sum([x[i]*(y[(i+1)%3]-y[(i+2)%3]) for i in range(3)]))
def l(x, y):
    return ((x[0]-x[2])**2 + (y[0]-y[2])**2)**0.5
def h(x, y):
    return vect(x, y) / l(x, y)

n = int(input())
x = []
y = []
for i in range(n):
    a, b = [int(x) for x in input().split()]
    x.append(a)
    y.append(b)
x += x[:2]
y += y[:2]

dmin = inf
for i in range(n):
    d = h(x[i:i+3], y[i:i+3])/2
    if dmin > d:
        dmin = d

print(dmin)
