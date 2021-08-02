#import math
t = int(input())
f = 0
for i in range(1, 50):
    for j in range(1, 50):
        k = pow(3, i) + pow(5, j)
        if k == t:
            print(i, j)
            return
print("-1")
