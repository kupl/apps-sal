import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n, k = list(map(int, input().split()))

    ANS = [[0] * n for i in range(n)]

    o = k // n
    m = k - o * n

    now = 0
    for i in range(n):
        if i < m:
            for j in range(o + 1):
                ANS[i][now] = 1
                now = (now + 1) % n

        else:
            for j in range(o):
                ANS[i][now] = 1
                now = (now + 1) % n

    if m == 0:
        print(0)
    else:
        print(2)

    for ans in ANS:
        print("".join(map(str, ans)))
