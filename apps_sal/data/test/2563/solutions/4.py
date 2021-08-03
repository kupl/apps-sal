import sys


def I():
    return sys.stdin.readline().rstrip()


for _ in range(int(I())):
    e, o, a = [], [], []
    for c in I():
        x = ord(c) - ord('0')
        if x & 1:
            o.append(x)
        else:
            e.append(x)
    i, j = 0, 0
    while i < len(o) or j < len(e):
        if i < len(o) and j < len(e):
            if o[i] < e[j]:
                a.append(chr(o[i] + ord('0')))
                i += 1
            else:
                a.append(chr(e[j] + ord('0')))
                j += 1
        elif i < len(o):
            a.append(chr(o[i] + ord('0')))
            i += 1
        else:
            a.append(chr(e[j] + ord('0')))
            j += 1
    print("".join(a))
