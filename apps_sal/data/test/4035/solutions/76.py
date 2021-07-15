import math

A, B = list(map(int, input().split()))
A_1 = math.ceil(A * 12.5)
A_2 = math.ceil((A + 1) * 12.5)

for i in range(A_1, A_2 + 1):
    if i == A_2:
        print(-1)
    elif math.floor(i * 0.1) != B:
        continue
    elif math.floor(i * 0.1) == B:
        print(i)
        break
