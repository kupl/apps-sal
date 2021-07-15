n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

ans = 'No'
for i in range(n - m + 1):
    for j in range(n - m + 1):
        if all([A[i + k][j:j + m] == B[k] for k in range(m)]):
            ans = 'Yes'
print(ans)
