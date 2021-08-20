import sys
input = sys.stdin.readline
for f in range(int(input())):
    (n, k) = map(int, input().split())
    if k >= n:
        print(k - n)
    else:
        x = k - n
        if x % 2 == 0:
            print(0)
        else:
            print(1)
