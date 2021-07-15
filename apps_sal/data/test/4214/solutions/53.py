import itertools
import math
N = int(input())


citys = []
for i in range(N):
    citys.append([int(x) for x in input().split()])

a = list(itertools.permutations(list(range(N)), N))

ans = 0
for i in a:
    b = 0
    for j in range(N-1):
        b += math.sqrt((citys[i[j]][0] - citys[i[j+1]][0])**2 + (citys[i[j]][1] - citys[i[j+1]][1])**2)
    ans += b

print((ans/len(a)))

