
import re
import inspect
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

class Spider():
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d

    def get_copy(self):
        return Spider(self.x, self.y, self.d)

    def move(self):
        if self.d == 'R':
            self.x += 1
        elif self.d == 'L':
            self.x -= 1
        elif self.d == 'U':
            self.y -= 1
        elif self.d == 'D':
            self.y += 1
        else:
            raise Exception('WHAT HAVE YOU DONE', self.d)

def main(i, n, m, lders, rders, uders):
    sightings = 0
    
    iders = [s for s in uders if s.x == i and s.y % 2 == 0]
    sightings += len(iders)
    prnt('id', len(iders))
   
    ulders = [s for s in rders if s.y == (i - s.x)]
    sightings += len(ulders)
    prnt('uld', len(ulders))
  
    urders = [s for s in lders if s.y == (s.x - i)]
    sightings += len(urders)
    prnt('urd', len(urders))
    
    return str(sightings)
        

def __starting_point():
    (n,m,k) = rints()
    field = [rstr() for i in range(n)]

    si = [0 for i in range(m)]
    spiders = []
    for j,row in enumerate(field):
        for i,space in enumerate(row):
            if space == 'R':
                if i+j < len(si):
                    si[i+j] += 1
            if space == 'L':
                if i-j >= 0:
                    si[i-j] += 1
            if space == 'U':
                if j % 2 == 0:
                    si[i] += 1

    print(' '.join([str(i) for i in si]))


__starting_point()
