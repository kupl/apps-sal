n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x: x[1] - x[0])
ans = 0
for i in range(n):
    ans += a[i][0] * i
    ans += a[i][1] * (n - i - 1)
print(ans)
