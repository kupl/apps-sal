n = int(input())

a = list(map(int, input().split()))

h = 0
ans = 0

for i in range(n):
    h = max(h, a[i])
    ans += h - a[i]


print(ans)
