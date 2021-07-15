N = int(input())
T = [0] * 5
for i in range(5):
    T[i] = int(input())

from math import ceil
t = min(T)
print(ceil(N/t) + 4)
