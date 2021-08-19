(n, m) = map(int, input().split())
p = [0] * (n + 1)
for i in range(m):
    (a, b) = map(int, input().split())
    p[a] += 1
    p[b] += 1
ans = 'unknown topology'
if n == m:
    if p.count(2) == n:
        ans = 'ring topology'
elif n == m + 1:
    if n - 1 in p:
        ans = 'star topology'
    elif p.count(1) == 2 and p.count(2) == n - 2:
        ans = 'bus topology'
print(ans)
