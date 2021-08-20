import math
(n, m) = list(map(int, input().split()))
f = 0
for i in range(n):
    v2 = [j for j in input().split()]
    for j in v2:
        if j == 'C' or j == 'M' or j == 'Y':
            f = 1
if f == 1:
    print('#Color')
else:
    print('#Black&White')
