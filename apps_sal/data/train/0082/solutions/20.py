import sys
import math
for _ in range(int(input())):
    n = int(input())
    a = [int(o) for o in input().split()]
    print(*a[::-1])
