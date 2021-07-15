#      
import collections, atexit, math, sys, bisect 

sys.setrecursionlimit(1000000)

isdebug = False
try :
    #raise ModuleNotFoundError
    import pywin32
    import numpy
    def dprint(*args, **kwargs):
        #print(*args, **kwargs, file=sys.stderr)
        # in python 3.4 **kwargs is invalid???
        print(*args,  file=sys.stderr)
    dprint('debug mode')
    isdebug = True
except Exception:
    def dprint(*args, **kwargs):
        pass


def red_inout():
    inId = 0
    outId = 0
    if not isdebug:
        inId = 0
        outId = 0
    if inId>0:
        dprint('use input', inId)
        try:
            f = open('input'+ str(inId) + '.txt', 'r')
            sys.stdin = f #标准输出重定向至文件
        except Exception:
            dprint('invalid input file')
    if outId>0:
        dprint('use output', outId)
        try:
            f = open('stdout'+ str(outId) + '.txt', 'w')
            sys.stdout = f #标准输出重定向至文件
        except Exception:
            dprint('invalid output file')
            
        atexit.register(lambda :sys.stdout.close())     #idle 中不会执行 atexit

if isdebug:
    red_inout()

def getIntList():
    return list(map(int, input().split()))            

def solve():    
    pass
    
T_ = 1    
#T_, = getIntList()

for iii_ in range(T_):
    #solve()
    w1,h1,w2,h2  = getIntList()
    r = w1+2
    r+= 2*h1
    r += w2+2
    r+= 2*h2
    r += w1-w2
    print(r)

    







