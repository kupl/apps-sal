n = int(input())
a = sorted(map(int, input().split(' ')))

ans = "NO"
for i in range(n - 2):
    if a[i] + a[i + 1] > a[i + 2]:
        ans = "YES"
print(ans)
