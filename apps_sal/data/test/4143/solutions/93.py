import math
N = int(input())
lsT = []
for i in range(5):
    lsT.append(int(input()))
print(4 + math.ceil(N / min(lsT)))
