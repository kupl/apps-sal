n = int(input())
l = list(map(int, input().split()))
ans = 0
c = n
for i in range(n - 1, -1, -1):
    if i < c:
        ans += 1
    c = min(c, i - l[i])
print(ans)
