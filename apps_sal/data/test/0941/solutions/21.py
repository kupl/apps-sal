import sys
import math
input = sys.stdin.readline

b, k = map(int, input().split())
l = list(map(int, input().split()))

if b % 2 == 1:
    count = 0
    for i in range(k):
        if l[i] % 2 == 1:
            count += 1

    if count % 2 == 0:
        print("even")
    else:
        print("odd")

else:
    if l[-1] % 2 == 0:
        print("even")
    else:
        print("odd")
