n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = []
if n % 2 == 1:
    ans.append(l[n // 2])
    for i in range(n // 2):
        ans.append(l[i])
        ans.append(l[(n + 1) // 2 + i])
else:
    for i in range(n // 2):
        ans.append(l[(n + 1) // 2 + i])
        ans.append(l[i])
num = 0
for i in range(1, n - 1):
    if ans[i] < min(ans[i - 1], ans[i + 1]):
        num += 1
print(num)
print(' '.join(map(str, ans)))
