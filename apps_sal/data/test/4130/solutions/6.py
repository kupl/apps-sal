import sys
I = sys.stdin.readline
b = [0] * 150003
n = I()
for i in map(int, I().split()):
    b[i] += 1
a = 0
for i in range(1, 150002):
    if b[i - 1] > 0:
        b[i - 1] -= 1
    elif b[i] > 0:
        b[i] -= 1
    elif b[i + 1] > 0:
        b[i + 1] -= 1
    else:
        a -= 1
    a += 1
print(a)
