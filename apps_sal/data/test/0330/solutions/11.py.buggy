from math import trunc
p, y = map(int, input().split())
if p ** 2 < y:
    st = p
else:
    st = trunc(y ** 0.5)
for i in range(y, p, -1):
    check = True
    for j in range(2, st + 1):
        if i % j == 0:
            check = False
            break
    if check:
        print(i)
        return
print(-1)
