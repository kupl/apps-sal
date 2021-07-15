import sys
n = int(input())
c = [-1] * (10**5+1)
for i in range(n):
    x,k = list(map(int,input().split()))
    if c[k] < x-1:
        print("NO")
        return
    else:
        c[k] = max(c[k],x)

print("YES")

