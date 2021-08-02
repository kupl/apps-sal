n = int(input())
h = [0] + list(map(int, input().split()))

ans = 0
for i in range(n):
    s = h[i + 1] - h[i]
    if s > 0:
        ans += s
print(ans)
