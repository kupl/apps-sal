import sys
def input():
    return sys.stdin.readline()[:-1]

T = int(input())


for i in range(T):
    flag = True
    n,m,k = list(map(int,input().split()))
    h = list(map(int,input().split()))
    for i in range(n-1):
        x=max(h[i+1]-k,0)
        if x-h[i]>m:
            flag = False
            break
        else:
            m -= x-h[i]
    if flag:
        print("YES")
    else:
        print("NO")
