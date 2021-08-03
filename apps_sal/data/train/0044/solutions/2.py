from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    x = 4 * n
    for i in range(n):
        print(x, end=" ")
        x -= 2
    print()
