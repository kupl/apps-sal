import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n, x = list(map(int, input().split()))
    ANS = 0

    for i in range(n - 1):
        u, v = list(map(int, input().split()))
        if u == x or v == x:
            ANS += 1

    if ANS <= 1:
        print("Ayush")
        continue

    if n % 2 == 0:
        print("Ayush")
    else:
        print("Ashish")
