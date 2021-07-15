s = input()
metals = []
heavys = []
ind = cur = -1
while True:
    cur = s.find('heavy', ind + 1)
    if cur != -1:
        heavys.append(cur)
        ind = cur
    else:
        break
ind = cur = -1
while True:
    cur = s.find('metal', ind + 1)
    if cur != -1:
        metals.append(cur)
        ind = cur
    else:
        break
ind = ans = 0
for x in metals:
    while ind < len(heavys) and heavys[ind] < x:
        ind += 1
    ans += ind
print(ans)
