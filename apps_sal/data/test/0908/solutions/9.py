n = int(input())
N = [0] + list(map(int, input().split()))

S = [[""] * 2 for i in range(n + 1)]

for i in range(1, n + 1):
    s = input()
    S[i] = [s, s[::-1]]

INF = 10 ** 15

F1 = [[INF] * 2 for i in range(n + 1)]
F2 = [[INF] * 2 for i in range(n + 1)]

F1[1][0] = 0
F1[1][1] = N[1]
F2[1][0] = 0
F2[1][1] = N[1]

for i in range(2, n + 1):
    if S[i][0] >= S[i - 1][0]:
        F1[i][0] = min(F1[i - 1][0], F2[i - 1][0])

    if S[i][0] >= S[i - 1][1]:
        F2[i][0] = min(F1[i - 1][1], F2[i - 1][1])

    if S[i][1] >= S[i - 1][0]:
        F1[i][1] = min(F1[i - 1][0], F2[i - 1][0]) + N[i]

    if S[i][1] >= S[i - 1][1]:
        F2[i][1] = min(F1[i - 1][1], F2[i - 1][1]) + N[i]


if min(F1[n][0], F1[n][1], F2[n][0], F2[n][1]) == INF:
    print(-1)
else:
    print(min(F1[n][0], F1[n][1], F2[n][0], F2[n][1]))
