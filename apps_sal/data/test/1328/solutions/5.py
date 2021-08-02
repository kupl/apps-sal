n, MA, MB = map(int, input().split())
INF = 10**10
A = []
B = []
C = []
for i in range(n):
    a, b, c = map(int, input().split())
    if MA * b - MB * a > 0:
        A.append([MA * b - MB * a, c])
    elif MA * b - MB * a < 0:
        B.append([MB * a - MA * b, c])
    else:
        C.append(c)
dp1 = [[INF] * 10010 for i in range(len(A) + 1)]
for i in range(1, len(A) + 1):
    for j in range(1, 10010):
        if j < A[i - 1][0]:
            dp1[i][j] = dp1[i - 1][j]
        elif j == A[i - 1][0]:
            dp1[i][j] = min(A[i - 1][1], dp1[i - 1][j])
        else:
            dp1[i][j] = min(dp1[i - 1][j], dp1[i - 1][j - A[i - 1][0]] + A[i - 1][1])
dp2 = [[INF] * 10010 for i in range(len(B) + 1)]
for i in range(1, len(B) + 1):
    for j in range(1, 10010):
        if j < B[i - 1][0]:
            dp2[i][j] = dp2[i - 1][j]
        elif j == B[i - 1][0]:
            dp2[i][j] = min(B[i - 1][1], dp2[i - 1][j])
        else:
            dp2[i][j] = min(dp2[i - 1][j], dp2[i - 1][j - B[i - 1][0]] + B[i - 1][1])
ans = INF
for i in range(10010):
    a = dp1[-1][i] + dp2[-1][i]
    if a < ans:
        ans = a
for i in range(len(C)):
    if C[i] < ans:
        ans = C[i]
if ans < INF:
    print(ans)
else:
    print(-1)
