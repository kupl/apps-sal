3
import sys
input = lambda: sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    if a[0] + a[1] <= a[-1]:
        print(1, 2, len(a))
    else:
        print(-1)

