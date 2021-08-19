import math
import sys
withFile = 0
if withFile == 1:
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')


def getl():
    if withFile == 0:
        return input()
    else:
        return fin.readline()


def printl(s):
    if withFile == 0:
        print(s)
    else:
        fout.write(str(s))


def get_arr():
    x = getl().split(' ')
    if x[-1] == '':
        x = x[:-1]
    return list(map(int, x))


n = get_arr()[0]
a = get_arr()
f = [1 for i in range(n)]
for i in range(n):
    if i == 0:
        continue
    if a[i] >= a[i - 1]:
        f[i] += f[i - 1]
print(max(f))
if withFile == 1:
    fin.close()
    fout.close()
