import math
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    print(math.ceil(n*m/2))




