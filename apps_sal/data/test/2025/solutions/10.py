from math import floor

q = int(input())
n = [int(input()) for i in range(0, q)]

for k in n:
    x = floor(k/4) - (k % 2)
    if x > 0 and k != 11:
        print(x)
    else:
        print(-1)

