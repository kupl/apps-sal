n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1

c = [0 for _ in range(100005)]

for i in range(n):
    val = a[i]
    c[val - 1] += 1
    c[val] += 1
    c[val + 1] += 1

ans = 0
for i in range(100005):
    ans = max(ans, c[i])

print(ans)
