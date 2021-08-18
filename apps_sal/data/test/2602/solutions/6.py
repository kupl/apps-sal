import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
t = int(input())
for _ in range(t):
    a, b, n, m = list(map(int, input().split()))
    if a + b < (n + m):
        print("No")
        continue
    if a <= b:
        if a >= m:
            print("Yes")
        else:
            print("No")
    else:
        if b >= m:
            print("Yes")
        else:
            print("No")
