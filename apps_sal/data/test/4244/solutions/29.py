n = int(input())
l = list(map(int, input().split()))
ans = 1000000
for p in range(1, 101):
    d = 0
    for x in l:
        d += (x - p) ** 2
    ans = min(d, ans)
print(ans)
