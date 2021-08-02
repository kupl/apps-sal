N = int(input())
a = list(map(int, input().split()))
sum = [0]
for i in range(0, N):
    sum.append(sum[-1] + a[i])
ans = abs(sum[N] - 2 * sum[1])
for i in range(1, N):
    ans = min(ans, abs(sum[N] - 2 * sum[i]))
print(ans)
