n = int(input())
h = list(map(int, input().split()))
ans, cur = 0, 0
for i in range(1, n):
    if h[i] <= h[i - 1]:
        cur += 1
    else:
        cur = 0
    ans = max(ans, cur)
print(ans)
