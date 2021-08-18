# Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys
import math
import queue
#sys.stdin = open("input.txt", "r")
MOD = 10**9 + 7

k = int(input())
f = []
i = 1
while i * i < k:
    if k % i == 0:
        f.append((i, k // i))
    i += 1
if i * i == k:
    f.append((i, i))
for i in range(len(f)):
    if f[i][0] >= 5 and f[i][1] >= 5:
        x = f[i][1]
        y = f[i][0]
        vow = ['a', 'e', 'i', 'o', 'u']
        ans = [[None for i in range(y)] for j in range(x)]
        for ii in range(x):
            for jj in range(y):
                ans[ii][jj] = vow[(ii + jj) % 5]
        string = []
        for row in ans:
            string += row
        print(''.join(string))
        return
print(-1)
