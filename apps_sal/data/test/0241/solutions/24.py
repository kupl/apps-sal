
import re
import inspect
from sys import argv, exit

def rstr():
    return input()

def rstrs(splitchar=' '):
    return [i for i in input().split(splitchar)]

def rint():
    return int(input())

def rints(splitchar=' '):
    return [int(i) for i in rstrs(splitchar)]

def varnames(obj, namespace=globals()):
    return [name for name in namespace if namespace[name] is obj]

def pvar(var, override=False):
    prnt(varnames(var), var)

def prnt(*args, override=False):
    if '-v' in argv or override:
        print(*args)

# Faster IO
pq = []
def penq(s):
    if not isinstance(s, str):
        s = str(s)
    pq.append(s)

def pdump():
    s = ('\n'.join(pq)).encode()
    os.write(1, s)

def __starting_point():
    timesteps, ast, mn, mx = rints()
    to_add = timesteps - ast
    asts = rints()
    for t in asts:
        if t < mn or t > mx:
            print('Incorrect')
            return
    if mn not in asts:
        if to_add == 0:
            print('Incorrect')
            return
        else:
            to_add -= 1

    if mx not in asts:
        if to_add == 0:
            print('Incorrect')
            return
        else:
            to_add -= 1

    print('Correct')

        

__starting_point()
