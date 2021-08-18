
import sys
input = sys.stdin.readline

n = int(input())

d = set()

for _ in range(n):
    i = input().strip()
    if i in d:
        print("YES")
    else:
        print("NO")
    d.add(i)
