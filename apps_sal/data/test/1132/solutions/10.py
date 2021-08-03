
import sys
import math
n, m = list(map(int, input().split()))

degree = [0] * (n + 1)

for _ in range(0, int(m)):
    a, b = list(map(int, input().split()))
    degree[a] = degree[a] + 1
    degree[b] = degree[b] + 1


if degree.count(1) == 2 and degree.count(2) == n - 2:
    print('bus topology')
elif degree.count(2) == n:
    print('ring topology')
elif degree.count(1) == n - 1 and degree.count(n - 1) == 1:
    print('star topology')
else:
    print('unknown topology')
