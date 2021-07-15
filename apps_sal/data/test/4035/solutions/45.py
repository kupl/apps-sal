import math
A, B = list(map(int, input().split()))

for i in range(int(100 / 0.08)):
    if math.floor(i * 0.08) == A and math.floor(i * 0.1) == B:
        print(i)
        return
print((-1))

