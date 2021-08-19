H = int(input())
s = 1
t = 0
while H > 1:
    H = H // 2
    s = s * 2
    t = t + 1
list = []
u = 1
while u <= t:
    list.append(u)
    u = u + 1
z = 0
for i in list:
    z = z + 2 ** (i - 1)
print(str(z + s))
