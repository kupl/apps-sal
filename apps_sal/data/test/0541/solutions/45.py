n, m = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(m)]
c.sort(key=lambda val: val[1])

left = 0
ans = 0
for i, [a, b] in enumerate(c):
    if left <= a:
        ans += 1
        left = b
print(ans)
