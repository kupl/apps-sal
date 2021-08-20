n = int(input())
a = list(map(int, input().split()))
ans = 1
max_ = 0
for i in range(n - 1):
    if a[i] > max_:
        max_ = a[i]
    if max_ <= i + 1:
        ans += 1
print(ans)
