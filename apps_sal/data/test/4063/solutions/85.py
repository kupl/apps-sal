n = int(input())
d = list(map(int, input().split()))
d.sort()
ans = 0
for i in range(1, 10**5 + 1):
    if d[n // 2 - 1] < i and d[n // 2] >= i:
        ans += 1

print(ans)
