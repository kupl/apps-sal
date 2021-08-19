import math
from sys import stdin
input = stdin.readline
for i in range(int(input())):
    (n, k) = map(int, input().split())
    print(['NO', 'YES'][n >= k * k and (n - k) % 2 == 0])
