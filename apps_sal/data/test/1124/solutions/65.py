import math
N = int(input())
l = list(map(int,input().split()))
g = 0
for i in range(N):
    g = math.gcd(g,l[i])
print(g)
