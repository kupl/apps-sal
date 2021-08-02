import math
withFile = 0

if(withFile == 1):
    fin = open('input.txt', 'r')
    fout = open('output.txt', 'w')


def getl():
    if(withFile == 0):
        return input()
    else:
        return fin.readline()


def printl(s):
    if(withFile == 0):
        print(s)
    else:
        fout.write(str(s))


def get_arr():
    x = getl().split(' ')
    if(x[-1] == ''):
        x = x[:-1]
    return list(map(int, x))


def f(x):
    if(x == 0):
        return 0
    d = 1
    while(d < x):
        d <<= 1
    if(d != x):
        d >>= 1
    return 1 + f(x - d)


x = get_arr()[0]

print(f(x))


if(withFile == 1):
    fin.close()
    fout.close()
