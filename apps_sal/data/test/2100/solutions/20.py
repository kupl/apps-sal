n = int(input())
l = r = 0

for i in range(n):
    a, b = list(map(int, input().split()))
    l += a
    r += b

ans = min(n - l, l) + min(n - r, r)
print(ans)
