n = int(input())
a = list(map(int, input().split()))
ans = 0
i = 0
while (i + 2 < n):
    if (a[i] >= 4 and a[i + 1] >= 4 and a[i + 2] >= 4):
        ans += 1
        i += 2
    i += 1
print(ans)
