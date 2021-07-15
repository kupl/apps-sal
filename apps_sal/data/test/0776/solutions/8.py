import sys

a, b, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

num_item = 0
cost = 0

usb_l = []
ps2_l = []

for i in range(m):
    val, type_p = sys.stdin.readline().split()
    val = int(val)

    if type_p[0] == 'U':
        usb_l.append(val)
    else:
        ps2_l.append(val)

usb_l.sort()
ps2_l.sort()

len_usb = len(usb_l)
len_ps2 = len(ps2_l)

usb_l.append(float('inf'))
ps2_l.append(float('inf'))

'''
print(usb_l, file=sys.stderr)
print(ps2_l, file=sys.stderr)
'''

pos1 = 0
pos2 = 0

if a > len_usb:
    num_item += len_usb
    cost += sum(usb_l[:-1])
    pos1 = len_usb
else:
    num_item += a
    cost += sum(usb_l[:a])
    pos1 = a

if b > len_ps2:
    num_item += len_ps2
    cost += sum(ps2_l[:-1])
    pos2 = len_ps2
else:
    num_item += b
    cost += sum(ps2_l[:b])
    pos2 = b

count = 0

while num_item < m and count < c:
    if usb_l[pos1] < ps2_l[pos2]:
        cost += usb_l[pos1]
        pos1 += 1
    else:
        cost += ps2_l[pos2]
        pos2 += 1

    num_item += 1
    count += 1

print(num_item, cost)
