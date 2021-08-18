import sys
input = sys.stdin.readline

n, m = map(int, input().split())
X = list(map(int, input().split()))

PLUS = [[0, 0] for i in range(n + 1)]

DIFF1 = [0] * (n + 1)
DIFF2 = [0] * (n + 1)


for i in range(m):
    if 0 <= i - 1:
        if X[i - 1] < X[i] - 1:
            DIFF1[X[i]] += abs(X[i - 1] + 1 - 1) - abs(X[i - 1] + 1 - X[i])

        elif X[i - 1] == X[i] - 1:
            DIFF1[X[i]] += abs(X[i - 1] + 1 - 1) - abs(1 - X[i])

        elif X[i - 1] >= X[i] + 1:
            DIFF1[X[i]] += abs(X[i - 1] - 1) - abs(X[i - 1] - X[i])

    if i + 1 < m:
        if X[i + 1] < X[i] - 1:
            DIFF1[X[i]] += abs(X[i + 1] + 1 - 1) - abs(X[i + 1] + 1 - X[i])

        elif X[i + 1] == X[i] - 1:
            DIFF1[X[i]] += abs(X[i + 1] + 1 - 1) - abs(1 - X[i])

        elif X[i + 1] >= X[i] + 1:
            DIFF1[X[i]] += abs(X[i + 1] - 1) - abs(X[i + 1] - X[i])


for i in range(m):
    if 0 <= i - 1:
        if X[i - 1] < X[i]:
            DIFF2[X[i]] += abs(X[i - 1] - X[i]) - abs(X[i - 1] + 1 - 1)

        elif X[i - 1] > X[i] + 1:
            DIFF2[X[i]] += abs(X[i - 1] - X[i] - 1) - abs(X[i - 1] - 1)

    if i + 1 < m:
        if X[i + 1] < X[i]:
            DIFF2[X[i]] += abs(X[i + 1] - X[i]) - abs(X[i + 1] + 1 - 1)

        elif X[i + 1] > X[i] + 1:
            DIFF2[X[i]] += abs(X[i + 1] - X[i] - 1) - abs(X[i + 1] - 1)


ANS = 0
for i in range(1, m):
    ANS += abs(X[i] - X[i - 1])

print(ANS, end=" ")

for i in range(2, n + 1):
    ANS += DIFF1[i] + DIFF2[i - 1]
    print(ANS, end=" ")
