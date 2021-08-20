(n, m) = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
ans = []
for i in range(m - 1):
    ans.append(abs(x[i] - x[i + 1]))
ans.sort(reverse=True)
print(sum(ans[n - 1:]))
