
import re
import inspect
from copy import copy
from sys import argv, exit

def rstr():
    return input()

def rint():
    return int(input())

def rints(splitchar=' '):
    return [int(i) for i in input().split(splitchar)]

def varnames(obj, namespace=globals()):
    return [name for name in namespace if namespace[name] is obj]

def pvar(var, override=False):
    prnt(varnames(var), var)

def prnt(*args, override=False):
    if '-v' in argv or override:
        print(*args)

def remove_split(l, i, j):
    prnt("Removed {} thru {}, {}".format(i, j, l[i:j]))
    new_l = l[:i] + l[j:]
    prnt("New List: {}".format(new_l))
    return new_l

def degrade(l, initial_size):
    i=0
    color = 0
    removed = False
    for j,x in enumerate(l):
        if not color:
            color = x
            i = j
        
        if color != x:
            if j-i >= 3:
                l = remove_split(l, i, j)
                removed = True
            color = x
            i = j
        if j == len(l)-1 and color == x and j-i >= 2:
            prnt('removing {} {}'.format(i, j))
            l = remove_split(l, i, j+1)
            removed = True

    if removed:
        prnt(l)
        return degrade(l, initial_size)
    else:
        return initial_size - len(l)


def __starting_point():
    (num, kolors, xolor) = rints()
    balls = rints()
    
    results = []
    for i in range(len(balls)):
        l = copy(balls)
        l.insert(i, xolor)
        pvar(l)
        results.append(degrade(l, len(l)-1))
    prnt(results)
    ans = max(results)
    if ans == -1:
        ans = 0
    print(ans)

__starting_point()
