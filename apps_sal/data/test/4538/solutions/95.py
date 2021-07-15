#ABC174 B

N,D = map(int,input().split())
import math
count = 0

for i in range(N):
    X = list(map(int,input().split()))
    S = math.sqrt(X[0]**2 + X[1]**2)
    if S <= D:
        count += 1

print(count)
