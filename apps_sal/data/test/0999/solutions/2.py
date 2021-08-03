n = int(input())
mx = 0
mn = 10 ** 10
for i in range(n):
    l, r = list(map(int, input().split(' ')))
    mx = max(mx, l)
    mn = min(mn, r)

m = int(input())
ans = 0
for i in range(m):
    l, r = list(map(int, input().split(' ')))
    ans = max([ans, mx - r, l - mn])
print(ans)
