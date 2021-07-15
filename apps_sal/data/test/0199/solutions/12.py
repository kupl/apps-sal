import math
n,s = list(map(int,input().split()))
v = input().split()
mini = math.inf
for i in range(n):
    mini = min(int(v[i]),mini)
s += mini*n
for i in range(n):
    s -= int(v[i])
if s < 0:
    print(mini)
elif s > mini*n:
    print(-1)
elif s%n == 0:
    print(mini-s//n)
else:
    print(mini-s//n-1)

