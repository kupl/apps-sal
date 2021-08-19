import math
(N, D) = list(map(int, input().split()))
num = math.floor(N / (D * 2 + 1))
if N % (D * 2 + 1) != 0:
    print(num + 1)
else:
    print(num)
