import sys
import math

input = sys.stdin.readline
flush = sys.stdout.flush

for _ in range(int(input())):
	n = int(input())
	print(1.0 / math.tan(math.pi / (2.0 * n)))

