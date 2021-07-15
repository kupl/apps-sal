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
    
N, = getIntList()
#print(N)
S = input()

za = getIntList()
bbb = 10 ** 20
dp = [0,bbb,bbb,bbb]

for i in range(N):
    dp1 = dp.copy()
    c = S[i]
    w = za[i]
    if c == 'h':
        dp1[1] = min(dp1[1], dp1[0])
        dp1[0] += w
    elif c == 'a':
        dp1[2] = min(dp1[2], dp1[1])
        dp1[1] += w
    elif c == 'r':
        dp1[3] = min(dp1[3], dp1[2])
        dp1[2] += w
    elif c=='d':
        dp1[3] += w
    dp = dp1
    #dprint(dp)
print(min(dp))




