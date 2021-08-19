n = int(input())
a = list(map(int, input().split()))
ans = sum(a)
for i in range(1, n - 1):
    if a[i] == 0 and a[i + 1] == 1 and (a[i - 1] == 1):
        ans += 1
print(ans)
