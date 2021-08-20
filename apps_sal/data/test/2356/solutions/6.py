import sys
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(*a)
