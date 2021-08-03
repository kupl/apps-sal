import sys
input = sys.stdin.readline

t = int(input())

for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    X = [0] * 32

    for a in A:
        for j in range(32, -1, -1):
            if a & (1 << j) != 0:
                X[j] += 1
                break

    ANS = 0

    for x in X:
        ANS += x * (x - 1) // 2

    print(ANS)
