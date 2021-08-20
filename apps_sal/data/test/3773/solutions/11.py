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


'\nK = 10\nN = 50\nV = 5\nfor k in range(V,V+1):\n    a = [0]*N\n    for i in range(1,N):\n        s = set()\n        for j in range(1,1+i//k):\n            s.add(a[i-j])\n        for j in range(N):\n            if j not in s:\n                a[i] = j\n                break\n    \n    #print(k,a)\n    #for i in range(N//V):\n    #    print(a[i*V:(i+1)*V])\n\n    \n    b = [grundy(i,k) for i in range(N)]\n    print(a)\n    print(b)\n    assert a==b\n'
readline = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10 ** 8)
(n,) = list(map(int, readline().split()))
g = 0
for _ in range(n):
    (a, k) = list(map(int, readline().split()))
    g ^= grundy(a, k)
if g:
    print('Takahashi')
else:
    print('Aoki')
