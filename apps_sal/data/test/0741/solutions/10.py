(n, k) = [int(i) for i in input().split()]
x = [0] + [int(i) for i in input().split()] + [k]
light = []
s = 0
e = 0
o = 0
even = []
odd = []
for i in range(len(x) - 1):
    s = x[i + 1] - x[i]
    light.append(s)
for i in range(len(light) - 1, -1, -1):
    if i % 2 == 0:
        e += light[i]
    else:
        o += light[i]
    even.append(e)
    odd.append(o)
even = even[::-1]
odd = odd[::-1]
sum = 0
m = 0
for i in range(len(light)):
    if light[i] != 1:
        if i % 2 == 0:
            if i + 1 >= len(light):
                m = max(light[i] - 1 + sum, m)
            else:
                m = max(sum + even[i + 1], m)
        elif i + 1 >= len(light):
            m = max(light[i] - 1 + sum, m)
        else:
            m = max(light[i] - 1 + sum + odd[i + 1], m)
    if i % 2 == 0:
        sum += light[i]
m = max(sum, m)
print(m)
