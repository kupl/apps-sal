(n, s) = list(map(int, input().split(' ')))
v0 = 0
fl = False
for i in range(n):
    (h, m) = list(map(int, input().split(' ')))
    v = h * 60 + m
    if i == 0 and v - 1 >= s:
        m2 = 0
        h2 = 0
        fl = True
        break
    elif (v - v0 - 2) // 2 >= s:
        v2 = v0 + s + 1
        m2 = v2 % 60
        h2 = v2 // 60
        fl = True
        break
    else:
        v0 = v
if fl:
    print(h2, m2)
else:
    m2 = (v0 + s + 1) % 60
    h2 = (v0 + s + 1) // 60
    print(h2, m2)
