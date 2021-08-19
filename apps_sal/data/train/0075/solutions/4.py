import sys
import math
input = sys.stdin.readline
flush = sys.stdout.flush
for _ in range(int(input())):
    n = int(input())
    print(2.0 * math.cos(math.pi / (4.0 * n)) / (2.0 * math.sin(math.pi / (2.0 * n))))
