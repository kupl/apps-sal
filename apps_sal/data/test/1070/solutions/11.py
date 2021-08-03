n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
count = 0
for i in range(1, n):
    if a[i] != a[i - 1]:
        count += 1
    if count > ans:
        ans = count
    if a[i] == a[i - 1]:
        count = 0
print(ans + 1)
