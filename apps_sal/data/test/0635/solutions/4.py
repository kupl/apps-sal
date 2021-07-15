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
    
N, S = getIntList()
z1 = getIntList()
z2 = getIntList()
#print(N)

if z1[0] ==0:
    print('NO')
    return

if z1[S-1] ==1:
    print('YES')
    return

if z2[S-1]==0:
    print('NO')
    return

for i in range(S-1, N):
    if z1[i] ==1 and z2[i]==1:
        print('YES')
        return

print('NO')







