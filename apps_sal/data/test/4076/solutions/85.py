from cmath import *
A, B, H, M = map(int, input().split())
print(abs(rect(A, pi * (H + M / 60) / 6) - rect(B, pi * M / 30)))
