from math import *


for t in range(int(input())):
    n, m = list(map(int, input().split()))
    print("W" + ("B" * (m - 1)))
    for i in range(1, n):
        print("B" * (m))
