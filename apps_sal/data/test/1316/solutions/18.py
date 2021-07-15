#      
import collections, atexit, math, sys, bisect 

sys.setrecursionlimit(1000000)
def getIntList():
    return list(map(int, input().split()))    

try :
    #raise ModuleNotFoundError
    import numpy
    def dprint(*args, **kwargs):
        #print(*args, **kwargs, file=sys.stderr)
        # in python 3.4 **kwargs is invalid???
        print(*args,  file=sys.stderr)
    dprint('debug mode')
except Exception:
    def dprint(*args, **kwargs):
        pass



inId = 0
outId = 0
if inId>0:
    dprint('use input', inId)
    sys.stdin = open('input'+ str(inId) + '.txt', 'r') #标准输出重定向至文件
if outId>0:
    dprint('use output', outId)
    sys.stdout = open('stdout'+ str(outId) + '.txt', 'w') #标准输出重定向至文件
    atexit.register(lambda :sys.stdout.close())     #idle 中不会执行 atexit
    
N, K = getIntList()
#print(N)
S = input()

nc = ' '
sss = 'abcdefghijklmnopqrstuvwxyz'
dr = dict()
for c in sss:
    dr[c] = 0
tn = 0
for x in S:
    if x!=nc:
        nc = x
        tn = 1
    else:
        tn+=1
    if K==tn:
        dr[x] +=1
        tn = 0

r = max( dr.values())
print(r)




