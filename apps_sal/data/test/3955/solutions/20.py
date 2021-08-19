(n, k, x) = list(map(int, input().split()))
lis = list(map(int, input().split()))
pre = [0] * (n + 2)
pos = [0] * (n + 2)
ans = 0
m = x ** k
for i in range(1, n):
    pre[i] = pre[i - 1] | lis[i - 1]
for i in range(n, 0, -1):
    pos[i] = pos[i + 1] | lis[i - 1]
for i in range(1, n + 1):
    ans = max(ans, pre[i - 1] | lis[i - 1] * m | pos[i + 1])
print(ans)
