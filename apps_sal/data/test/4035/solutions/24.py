import math
A, B = map(int, input().split())
b1 = B*10
b2 = b1 + 10

for i in range(b1, b2):
    if math.floor(i*0.08) == A:
        print(i)
        break

    if i == b2-1:
        print(-1)
