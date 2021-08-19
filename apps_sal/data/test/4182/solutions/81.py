(N, M, X, Y) = map(int, input().split())
x_lis = list(map(int, input().split()))
y_lis = list(map(int, input().split()))
x_max = max(x_lis)
y_min = min(y_lis)
ans = 'War'
for Z in range(X + 1, Y + 1):
    if x_max < Z <= y_min:
        ans = 'No War'
print(ans)
