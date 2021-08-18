"""
def grundy(a,k): 
    if a < k:
        return 0
    if a%k==0:
        return a//k
    q = a//k
    return grundy(a-1-q,k)
"""
import sys


def grundy(a, k):
    if a < k:
        return 0
    q = a // k
    r = (a - q * k) % (q + 1)
    if r == 0:
        return a // k
    v = (a - q * k) // (q + 1) + 1
    return grundy(a - (q + 1) * v, k)


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
    

    
    b = [grundy(i,k) for i in range(N)]
    print(a)
    print(b)
    assert a==b
"""
readline = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10**8)

n, = list(map(int, readline().split()))
g = 0
for _ in range(n):
    a, k = list(map(int, readline().split()))
    g ^= grundy(a, k)
if g:
    print("Takahashi")
else:
    print("Aoki")
