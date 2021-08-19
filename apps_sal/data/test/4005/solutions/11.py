import sys

sin = sys.stdin

w = sin.readline().split()
w = [int(x) for x in w]
b1 = sin.readline().split()
b1 = [int(x) for x in b1]
b2 = sin.readline().split()
b2 = [int(x) for x in b2]


def reduce(w, b):
    # Fully covered:
    if b[0] <= w[0] and b[1] <= w[1] and b[2] >= w[2] and b[3] >= w[3]:
        return True
    if b[0] <= w[0] and b[1] <= w[1]:
        if b[2] >= w[2] and b[3] >= w[1]:
            w[1] = b[3]
        if b[3] >= w[3] and b[2] >= w[0]:
            w[0] = b[2]
    elif b[2] >= w[2] and b[3] >= w[3]:
        if b[1] <= w[1] and b[0] <= w[2]:
            w[2] = b[0]
        if b[0] <= w[0] and b[1] <= w[3]:
            w[3] = b[1]


flag = False
if reduce(w, b1):
    print("NO")
    flag = True
elif not flag and reduce(w, b2):
    print("NO")
    flag = True
if not flag:
    print("YES")
