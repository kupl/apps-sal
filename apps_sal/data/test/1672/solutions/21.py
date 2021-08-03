n = int(input())
a = []
ans = 1
for i in range(n):
    num = int(input())
    a.append(num)
for i in range(1, n):
    if a[i] != a[i - 1]:
        ans += 1
print(ans)
