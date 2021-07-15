a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

c_left = c
while c_left >= 0:
    if c_left % b == 0:
        print("Yes")
        break
    c_left -= a
if c_left < 0:
    print("No")

