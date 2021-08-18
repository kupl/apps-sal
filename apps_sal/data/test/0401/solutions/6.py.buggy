a, b = list(map(int, input().split()))

mas1 = list(map(int, input().split()))
mas2 = list(map(int, input().split()))

min1 = min(mas1)
min2 = min(mas2)

heh = 10

for i in mas1:
    for j in mas2:
        if i == j and i < heh:
            heh = i
if heh != 10:
    print(heh)
    return
if min1 < min2:
    print(str(min1) + str(min2))
else:
    print(str(min2) + str(min1))
