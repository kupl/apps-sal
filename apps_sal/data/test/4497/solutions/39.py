import math

N = int(input())

i = 1
while i < N:
    i = i * 2

if i <= N:
    print(i)
else:
    print(math.floor(i / 2))
