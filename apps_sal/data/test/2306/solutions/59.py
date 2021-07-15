import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

N = int(input())
T = list(map(int,input().split()))
V = list(map(int,input().split()))

def calc_area(v1,v2,t,lim):
    if v1 > v2:
        v1,v2 = v2,v1
    if v2 == lim:
        if lim - v1 < t:
            return t*lim - (lim - v1)*(lim - v1)/2
        else:
            return (v1 + v2)*t/2
    else:
        if 2*lim - v1 - v2 < t:
            return t*lim - (lim - v1)*(lim - v1)/2 - (lim - v2)*(lim - v2)/2
        else:
            mid = (t + v2 - v1)/2
            return (mid + 2*v1)*mid/2 + (t - mid + 2*v2)*(t - mid)/2

def calc(N,T,V,maxv):
    ans = 0
    v = 0
    for i in range(N):
        next_v = min(v + T[i],maxv[i])
        ans += calc_area(v,next_v,T[i],V[i])
        v = next_v
    return ans

maxV = [0] * N
for i in range(N - 2,-1,-1):
    maxV[i] = min(maxV[i + 1] + T[i + 1],V[i],V[i + 1])
ans = calc(N,T,V,maxV) 
print(ans)
