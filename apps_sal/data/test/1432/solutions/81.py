n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
ans = [0] * n
ans[0] = sum_a - 2 * sum(a[1:n - 1:2])
for i in range(1, n):
    ans[i] = 2 * a[i - 1] - ans[i - 1]
print(*ans)
