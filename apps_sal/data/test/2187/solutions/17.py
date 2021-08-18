import sys
input = sys.stdin.readline


t = int(input())
for tests in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    M = [A[0]]
    for a in A[1:]:
        M.append(max(M[-1], a))

    A.append(M[-1])

    ANS = 0
    for i in range(n):
        if A[i] > A[i + 1]:
            continue
        else:
            ANS += min(M[i], A[i + 1]) - A[i]

    print(ANS)
