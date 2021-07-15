import sys
input = sys.stdin.readline

def judge(i, x):
    return V[i]-(T_acc[x+1]-T_acc[i])>0

def binary_search(i):
    l, r = 0, N
    
    while l<=r:
        mid = (l+r)//2
        
        if judge(i, mid):
            l = mid+1
        else:
            r = mid-1

    return r

N = int(input())
V = list(map(int, input().split()))
T = list(map(int, input().split()))
T.append(10**18)
T_acc = [0]

for Ti in T:
    T_acc.append(T_acc[-1]+Ti)

last = [0]*(N+1)
imos = [0]*(N+1)

for i in range(N):
    mark = binary_search(i)
    last[mark+1] += V[i]-(T_acc[mark+1]-T_acc[i])
    imos[i] += 1
    imos[mark+1] -= 1

for i in range(N):
    imos[i+1] += imos[i]

for i in range(N):
    ans = imos[i]*T[i]+last[i]
    
    if i<N-1:
        print(ans, end=' ')
    else:
        print(ans)
