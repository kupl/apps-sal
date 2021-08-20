(n, a, b) = map(int, input().split())
V = list(map(int, input().split()))
V.sort(reverse=True)
A = V[:a]
B = V[:b]
ave = sum(A) / a
print(ave)
C = [[0] * 51 for _ in range(51)]
C[0][0] = 1
for i in range(50):
    C[i + 1][0] = 1
    C[i + 1][i + 1] = 1
    for j in range(i):
        C[i + 1][j + 1] = C[i][j] + C[i][j + 1]
if A[0] == A[-1]:
    ans = 0
    x = V.count(A[0])
    for i in range(a, b + 1):
        if i <= x:
            ans += C[x][i]
else:
    x = V.count(A[-1])
    y = A.count(A[-1])
    ans = C[x][y]
print(ans)
