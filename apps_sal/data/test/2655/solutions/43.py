n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
p = 0
ans = 0
for i in range(n):
    if i == 0:
        continue
    ans += a[p]
    if i % 2 == 1:
        p += 1
print(ans)
