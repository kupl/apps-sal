import sys
input = sys.stdin.readline
t = int(input())
for tests in range(t):
    (a, b, n) = list(map(int, input().split()))
    ANS = 0
    while a <= n and b <= n:
        if a < b:
            a += b
        else:
            b += a
        ANS += 1
    print(ANS)
