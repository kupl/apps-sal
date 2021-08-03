from collections import *
x = sum(i % 2for i in list(Counter(input()).values()))
print("SFeicrosntd"[x % 2 + (x < 1)::2])
