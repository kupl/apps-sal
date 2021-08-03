import sys
input = sys.stdin.readline

t = int(input())
for testcases in range(t):
    n, p, k = list(map(int, input().split()))
    A = sorted((list(map(int, input().split()))))

    S = [0] * (n + k + 3)

    for i in range(n):
        S[i] = S[i - k] + A[i]

    # print(S)

    ANS = -1
    for i in range(n):
        if S[i] <= p:
            ANS = i

    print(ANS + 1)
