import statistics
import math

N = int(input())

min_x = []
max_x = []

for i in range(N):
    A, B = list(map(int, input().split()))
    min_x.append(A)
    max_x.append(B)

min_x.sort()
max_x.sort()

result = []

if len(min_x) % 2 == 0:
    min_median = (min_x[len(min_x) // 2 - 1] + min_x[len(min_x) // 2])
    max_median = (max_x[len(min_x) // 2 - 1] + max_x[len(min_x) // 2])
    print((len(list(range(math.floor(min_median), math.ceil(max_median) + 1)))))

else:
    min_median = min_x[len(min_x) // 2]
    max_median = max_x[len(min_x) // 2]
    print((max_median - min_median + 1))
