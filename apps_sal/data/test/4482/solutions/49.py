n = int(input())
a = list(map(int, input().split()))
inf = float('inf')
ans = inf
for b in range(-100, 101):
    ch = 0
    for i in range(n):
        ch += (b - a[i]) ** 2
    ans = min(ans, ch)
print(ans)
