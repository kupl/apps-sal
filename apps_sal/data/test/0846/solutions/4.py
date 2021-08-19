(n, m) = map(int, input().split())
a = list(map(int, input().split()))
ans = [0] * n
for i in range(m):
    b = a[i] - 1
    j = b
    while j < n and ans[j] == 0:
        ans[j] = b + 1
        j += 1
print(*ans)
