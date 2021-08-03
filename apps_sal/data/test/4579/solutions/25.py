n = int(input())
a = []

for i in range(n):
    a.append(input())

a.sort()
ans = 1

for i in range(n - 1):
    if a[i] != a[i + 1]:
        ans += 1

print(ans)
