from math import log2
t = int(input())
for _ in range(t):
    n = int(input())
    ct = 0
    for i in range(int(log2(n)) + 1):
        ct += n // (2 ** i)
    print(ct)
