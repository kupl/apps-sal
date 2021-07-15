n = int(input())
x_y = []
for _ in range(n):
  x_y.append([int(i) for i in input().split()])
import itertools
import math
ans = 0.0
for x_yi in itertools.permutations(x_y, n):
  sum_ = 0.0
  for i in range(n-1):
    sum_ += math.sqrt((x_yi[i][0] - x_yi[i+1][0]) ** 2 +
                      (x_yi[i][1] - x_yi[i+1][1]) ** 2)
  ans += sum_ / math.factorial(n)
print(ans)
