n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
for i in range(n - 1, -1, -1):
    count = 0
    for j in range(i, n, i + 1):
        count += ans[j]
    if count % 2 != a[i]:
        ans[i] = 1

if sum(ans) == 0:
    print(0)
    return

print(sum(ans))
for i in range(n):
    if ans[i] == 1:
        print(i + 1, end=" ")
