a, b = list(map(int, input().split()))
m = 100000
for i in range(int(input())):
    x, y, v = list(map(int, input().split()))
    d = (x - a) * (x - a) + (y - b) * (y - b)
    d = d**0.5
    t = abs(d / v)
    # print(d,t)
    if t < m:
        m = t
print(m)
