"""
def grundy(a,k): #石 a 個、最大 x//k までとれる
    #print(a,k)
    if a < k:
        return 0
    if a%k==0:
        return a//k
    q = a//k
    #v = (a-q*k)//q - (1 if (a-q*k)%q==0 else 0)
    return grundy(a-1-q,k)
"""
def grundy(a,k): #石 a 個、最大 x//k までとれる
    #print(a,k)
    if a < k:
        return 0
    q = a//k
    r = (a-q*k)%(q+1)
    if r==0:
        return a//k
    v = (a-q*k)//(q+1) + 1
    #print(a,k,q,v)
    return grundy(a-(q+1)*v,k)


"""
K = 10
N = 50
V = 5
for k in range(V,V+1):
    a = [0]*N
    for i in range(1,N):
        s = set()
        for j in range(1,1+i//k):
            s.add(a[i-j])
        for j in range(N):
            if j not in s:
                a[i] = j
                break
    
    #print(k,a)
    #for i in range(N//V):
    #    print(a[i*V:(i+1)*V])

    
    b = [grundy(i,k) for i in range(N)]
    print(a)
    print(b)
    assert a==b
"""
# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10**8)

n, = list(map(int,readline().split()))
g = 0
for _ in range(n):
    a,k = list(map(int,readline().split()))
    g ^= grundy(a,k)
if g:
    print("Takahashi")
else:
    print("Aoki")






