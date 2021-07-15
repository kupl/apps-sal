n = input()
s = list(input())

x, y = 0, 0
k = 0

cc = 0

for m in s:
    nk = k
    if m == 'U':
        y += 1
    elif m == 'R':
        x += 1
    if y > x:
        nk = 1
    elif y < x:
        nk = -1
    if nk * k == -1:
        cc += 1
    k = nk

print(cc)





