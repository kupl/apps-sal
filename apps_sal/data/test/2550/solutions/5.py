from math import *

T = int(input())
while T:
    T -= 1
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if sum(a) >= m:
        print(m)
    else:
        print(sum(a))
