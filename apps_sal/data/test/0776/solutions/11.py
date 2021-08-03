from sys import stdin

A, B, C = list(map(int, stdin.readline().split()))
M = int(stdin.readline())

usb_mouses = []
ps2_mouses = []
for m in range(M):
    p, t = stdin.readline().split()

    if t == "USB":
        usb_mouses.append(int(p))
    elif t == "PS/2":
        ps2_mouses.append(int(p))

usb_mouses.sort()
ps2_mouses.sort()

usb_cur = 0
ps2_cur = 0

cost = 0

while usb_cur < len(usb_mouses) and A > 0:
    cost += usb_mouses[usb_cur]
    usb_cur += 1
    A -= 1

while ps2_cur < len(ps2_mouses) and B > 0:
    cost += ps2_mouses[ps2_cur]
    ps2_cur += 1
    B -= 1

while C > 0:
    if usb_cur < len(usb_mouses) and ps2_cur < len(ps2_mouses):
        if usb_mouses[usb_cur] < ps2_mouses[ps2_cur]:
            cost += usb_mouses[usb_cur]
            usb_cur += 1
        else:
            cost += ps2_mouses[ps2_cur]
            ps2_cur += 1
    elif usb_cur < len(usb_mouses):
        cost += usb_mouses[usb_cur]
        usb_cur += 1
    elif ps2_cur < len(ps2_mouses):
        cost += ps2_mouses[ps2_cur]
        ps2_cur += 1
    else:
        break

    C -= 1

print("{} {}".format(usb_cur + ps2_cur, cost))
