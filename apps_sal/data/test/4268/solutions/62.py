from math import floor, sqrt
n,d=map(int,input().split())
X = []
def f(i,j):
    sm = 0
    for k in range(d):
        sm += (X[i][k]-X[j][k])**2
    return floor(sqrt(sm))**2 == sm
for _ in range(n):
    X.append(list(map(int,input().split())))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if f(i,j):
            ans += 1
print(ans)
