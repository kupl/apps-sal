import sys
import numpy as np
input = sys.stdin.readline
H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]

#import random
#H,W = 80, 80
#A = [[random.randint(0,80) for x in range(W)] for y in range(H)]
#B = [[random.randint(0,80) for x in range(W)] for y in range(H)]

C = [[abs(a - b) for a, b in zip(la, lb)] for la, lb in zip(A, B)]

MAX = 160 * (80 + 80) + 10
vals = np.zeros((W, MAX)).astype(bool)
temp = np.zeros(MAX).astype(bool)
temp[C[0][0]] = True
for y in range(H):
    for x in range(W):
        c = C[y][x]
        if c == 0:
            if y > 0:
                temp |= vals[x]
            if x > 0:
                temp |= vals[x - 1]
            vals[x] &= False
            vals[x] |= temp
            temp &= False
        else:
            if y > 0:
                temp[c:] |= vals[x][:-c]
                temp[:c + 1] |= vals[x][:c + 1][::-1]
                temp[:-c] |= vals[x][c:]
            if x > 0:
                temp[c:] |= vals[x - 1][:-c]
                temp[:c + 1] |= vals[x - 1][:c + 1][::-1]
                temp[:-c] |= vals[x - 1][c:]
            vals[x] &= False
            vals[x] |= temp
            temp &= False

print((np.where(vals[W - 1])[0][0]))
