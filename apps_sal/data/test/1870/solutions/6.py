n, c = map(int, input().split())
ans = 1
A = list(map(int, input().split()))
for j in range(1, n):
    if A[j] - A[j - 1] > c:
        ans = 1
    else:
        ans += 1
print(ans)
