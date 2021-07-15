import math
A, B, C, D = list(map(int, input().split()))
print(("Yes" if math.ceil(A/D) >= math.ceil(C/B) else "No"))

