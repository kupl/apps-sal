# import sys 
# import os
# import time
# from DataStructs import FenwickTree, SegTree, DWGraph
from _ast import arg, GtE
withFile = 0

if(withFile == 1):
    fin     = open('input.txt', 'r')
    fout    = open('output.txt', 'w')

def getl():
    nonlocal withFile
    if(withFile == 0):
        return input()
    else:
        return fin.readline()
    
def printl(s):
    nonlocal withFile
    if(withFile == 0):
        print(s)
    else:
        fout.write(str(s))

def get_arr():
    nonlocal withFile
    x = getl().split(' ')
    if(x[-1] == ''):
        x.pop()
    return list(map(int, x))

def __starting_point():
#     die(12)
    n = get_arr()[0]
    a   = sorted([[x, i] for i, x in enumerate(get_arr())])
    res = 0
    for i in range(1, len(a)):
        res += abs(a[i][1] - a[i-1][1])
    print(res)
    
if(withFile == 1):
    fin.close()
    fout.close()
__starting_point()
