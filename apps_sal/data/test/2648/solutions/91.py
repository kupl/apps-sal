n = int(input())
a = sorted(list(map(int, input().split())))
ans = 0
for i in range(1, len(a)):
    if a[i] == a[i - 1]:
        ans += 1
print(n - (ans + 1) // 2 * 2)
