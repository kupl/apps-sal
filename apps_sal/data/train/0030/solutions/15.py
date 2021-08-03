import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n = int(input())
    S = input().strip()

    A = 0
    for i in range(1, n):
        if S[i] == S[i - 1]:
            A += 1

    print((A + 1) // 2)
