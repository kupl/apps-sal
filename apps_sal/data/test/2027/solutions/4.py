n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
for i in range(n - 1, -1, -1):
    if i == n - 1:
        ans[i] = a[i]
    else:
        ans[i] = a[i] + a[i + 1]
for i in ans:
    print(i, end=' ')
