# list(map(int, input().split()))

n = int(input())
A = []
for x in range(n):
    A.append(input())
ans = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if(A[i][j] == 'X' and A[i + 1][j - 1] == 'X' and A[i - 1][j + 1] == 'X' and A[i + 1][j + 1] == 'X' and A[i - 1][j - 1] == 'X'):
            ans += 1
print(ans)
