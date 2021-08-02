import math
A, B = map(int, input().split())
if B == 1:
    N = 0
elif A < B:
    N = math.ceil((B - A) / (A - 1)) + 1
else:
    N = 1

print(N)
