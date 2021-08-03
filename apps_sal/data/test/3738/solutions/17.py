import sys
ox, oy = map(int, sys.stdin.readline().split())  # original position
s = sys.stdin.readline()
h = 0
v = 0
# here we calculate the distance to target position after one simulation
for i in range(len(s)):
    if s[i] == 'R':
        h += 1
    if s[i] == 'L':
        h -= 1
    if s[i] == 'U':
        v += 1
    if s[i] == 'D':
        v -= 1


def bs(l, r, a, b, rx, ry):
    l1 = l
    r1 = r
    a1 = a
    b1 = b
  #  print("ox:",a," oy:",b)
    while (l1 <= r1):
        mid = (l1 + r1) // 2
        a1 = a + h * mid
        b1 = b + v * mid
        # print ("   a1:",a1," b1:",b1)
        # print ("   l1:",l1," r1:",r1)
        # print ("   mid:",mid)
        if (rx == a1 and ry == b1):
            return 0
        if (rx - a1) * h == 0:
            if (ry - b1) * v > 0:
                l1 = mid + 1
            elif (ry - b1) * v < 0:
                r1 = mid - 1
            else:
                return -1

        if (ry - b1) * v == 0:
            if (rx - a1) * h > 0:
                l1 = mid + 1
            elif (rx - a1) * h < 0:
                r1 = mid - 1
            else:
                return -1

        if (rx - a1) * h != 0 and (ry - b1) * v != 0:
            if (rx - a1) * h > 0 and (ry - b1) * v > 0:
                l1 = mid + 1
            elif (rx - a1) * h < 0 and (ry - b1) * v < 0:
                r1 = mid - 1
            else:
                return -1
    return -1


a = 0
b = 0
pos = bs(0, 10**9, a, b, ox, oy)
kt = False
if pos == 0:
    print("Yes")
    kt = True
if kt == False:
    for i in range(len(s)):
        if s[i] == 'R':
            a += 1
        if s[i] == 'L':
            a -= 1
        if s[i] == 'U':
            b += 1
        if s[i] == 'D':
            b -= 1
        pos = bs(0, 10**9, a, b, ox, oy)
        if pos == 0:
            print("Yes")
            kt = True
            break
if kt == False:
    print("No")
