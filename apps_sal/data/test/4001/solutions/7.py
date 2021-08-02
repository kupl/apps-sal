import math
from collections import Counter
n = int(input())
A = list(map(int, input().split()))
x = max(A)

counter = Counter(A)

xr = math.ceil(math.sqrt(x))

LIST = []
for i in range(1, xr + 1):
    if x % i == 0:
        LIST.append(i)
        LIST.append(x // i)

LIST = set(LIST)

for l in LIST:
    counter[l] -= 1

REST = [i for i in list(counter.keys()) if counter[i] != 0]
y = max(REST)

print(x, y)
