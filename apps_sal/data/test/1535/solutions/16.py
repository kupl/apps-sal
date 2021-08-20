inStr = input()
n = int(inStr.split()[0])
x0 = int(inStr.split()[1])
y0 = int(inStr.split()[2])
s = set()
inf = 1e+19
for i in range(n):
    inStr = input()
    x = int(inStr.split()[0])
    y = int(inStr.split()[1])
    if x == x0:
        k = inf
        b = x0
    else:
        k = (y - y0, x - x0)
        k = k[0] / k[1]
        b = y0 - k * x0
    s.add((k, b))
print(len(s))
