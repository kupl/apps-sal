n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(n):
    if l[i] != l[0]:
        ans = max(i - 0, ans)
    if l[i] != l[n - 1]:
        ans = max(ans, n - i - 1)
print(ans)
