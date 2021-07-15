n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(0, n):
    for j in range(i + 1, n):
        if a[j] - a[i] == j - i:
            if a[j] == 1000 or a[i] == 1 and not (a[j] == 1000 and a[i] == 1):
                ans = max(j - i, ans)
            if a[j] == 1000 and a[i] == 1:
                ans = 1000
            else:
                ans = max(j - i - 1, ans)
print(ans)

