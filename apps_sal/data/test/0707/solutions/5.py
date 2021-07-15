from math import gcd
n,m = list(map(int,input().split()))

X = list(map(int, input().split()))

P = list(map(int,input().split()))

g = X[1]-X[0]

for i in range(n-1):
    g = gcd(g, X[i+1] - X[i])


for i,j in enumerate(P):
    if g % j == 0:
        print("YES")
        print(X[0],i+1)
        return
print("NO")

