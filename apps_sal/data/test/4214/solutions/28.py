from itertools import permutations
import math
n = int(input())
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split(' '))
    x.append(xi)
    y.append(yi)

l = [i for i in range(n)]
route = list(permutations(l))
length = 0
for ls in route:
    for i in range(n-1):
        length += math.sqrt((x[ls[i+1]]-x[ls[i]])**2+(y[ls[i+1]]-y[ls[i]])**2)
ans = length/math.factorial(n)
print(ans)
