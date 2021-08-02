import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

A.sort()

ANS = [0] * n

NOW = 1
for i in range(n):
    if ANS[i] == 0:
        ANS[i] = NOW

        for j in range(i, n):
            if A[j] % A[i] == 0 and ANS[j] == 0:
                ANS[j] = NOW

        NOW += 1

print(max(ANS))
