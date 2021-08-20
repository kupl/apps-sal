import sys
input = sys.stdin.readline
(n, x, y) = list(map(int, input().split()))
A = list(map(int, input().split()))
if x > y:
    print(n)
else:
    count = 0
    for a in A:
        if a <= x:
            count += 1
    print((count + 1) // 2)
