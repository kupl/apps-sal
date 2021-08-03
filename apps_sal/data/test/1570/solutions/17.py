import sys


k, n, w = map(int, input().split(" "))
if(k * (w) * (w + 1) / 2 < n):
    print(0)
    return
print(int(k * (w) * (w + 1) / 2 - n))
