read = lambda: list(map(int, input().split()))
n, d = read()
a = [list(map(int, input())) for i in range(d)]
ans = 0
d = 0
for i in a:
    if sum(i) < n: d += 1
    else:
        ans = max(ans, d)
        d = 0
ans = max(ans, d)
print(ans)

