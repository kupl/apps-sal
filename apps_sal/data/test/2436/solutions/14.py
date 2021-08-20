import sys
max_int = 1000000001
min_int = -max_int
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    ans = 0
    for (num, one) in enumerate(a, 1):
        if num >= one:
            ans = num
    print(ans + 1)
