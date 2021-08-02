n = int(input())
a = [0, 0] + [int(x) for x in input().split()]
ans = [0] * (n + 1)
for i in range(n, 1, -1):
    if ans[i] == 0:
        ans[i] = 1
    ans[a[i]] += ans[i]
if n == 1:
    ans[1] = 1
ans = ans[1:]
ans.sort()
print(*ans)
