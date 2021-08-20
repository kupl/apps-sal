n = int(input())
b = list(map(int, input().split()))
ans = [None] * n
for i in range(n // 2):
    if i == 0:
        ans[0] = 0
        ans[n - 1] = b[0]
    else:
        x = b[i] - ans[i - 1]
        if x > ans[n - i]:
            ans[n - i - 1] = ans[n - i]
            ans[i] = b[i] - ans[n - i - 1]
        else:
            ans[i] = ans[i - 1]
            ans[n - i - 1] = b[i] - ans[i]
for i in ans:
    print(i, end=' ')
