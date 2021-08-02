n = int(input())
a = []
for i in input():
    a.append(i)
r, d = 0, 0
was_r, was_d = True, True
while True:
    if was_r and was_d:
        was_r, was_d = False, False
    else:
        break
    for i in range(len(a)):
        if a[i] == "R":
            was_r = True
            if r != 0:
                r -= 1
                a[i] = 0
            else:
                d += 1
        elif a[i] == "D":
            was_d = True
            if d != 0:
                d -= 1
                a[i] = 0
            else:
                r += 1
if was_r:
    print("R")
else:
    print("D")
