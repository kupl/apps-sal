import itertools
import math
N = int(input())
lst1 = []
for _ in range(N):
    x, y = map(int, input().split())
    lst1.append((x, y))

lst2 = list(itertools.combinations(lst1, 2))
p = math.factorial(N) * (N - 1)
c = len(list(itertools.combinations(lst1, 2)))
total = 0

for i in lst2:
    d = ((i[1][0] - i[0][0]) ** 2 + (i[1][1] - i[0][1]) ** 2) ** 0.5
    total += d

num = int(p / c)
fct = math.factorial(N)

print(total * num / fct)
