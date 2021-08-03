import sys
input = sys.stdin.readline

t = int(input())
for tests in range(t):
    n, k = list(map(int, input().split()))
    S = input().strip()

    A = []

    X = 0
    for s in S:
        if s == "0":
            X += 1
        else:
            A.append(X)
            X = 0
    if X != 0:
        A.append(X)

    if len(A) == 1 and A[0] == n:
        print(1 + (n - 1) // (k + 1))
        continue

    ANS = 0
    if S[0] == "0" and S[-1] == "0":
        ANS += A[0] // (k + 1) + A[-1] // (k + 1)

        for i in range(1, len(A) - 1):
            ANS += (A[i] - k) // (k + 1)

    elif S[0] == "0":
        ANS += A[0] // (k + 1)

        for i in range(1, len(A)):
            ANS += max(0, A[i] - k) // (k + 1)

    elif S[-1] == "0":
        ANS += A[-1] // (k + 1)

        for i in range(len(A) - 1):
            ANS += max(0, A[i] - k) // (k + 1)

    else:
        for i in range(len(A)):
            ANS += max(0, A[i] - k) // (k + 1)

    print(ANS)
