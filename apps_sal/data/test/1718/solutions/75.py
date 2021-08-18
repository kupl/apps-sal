
import math

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))


cn = 1


Z = N - K

cn = cn + math.ceil(Z / (K - 1))

print(cn)
