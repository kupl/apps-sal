from itertools import permutations
import math
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
p = list(permutations(range(n), n))
ans = 0
for i in p:
    for j in range(n - 1):
        ans += ((l[i[j + 1]][0] - l[i[j]][0]) ** 2 + (l[i[j + 1]][1] - l[i[j]][1]) ** 2) ** 0.5
print(ans / math.factorial(n))
