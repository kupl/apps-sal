n, k = list(map(int, input().split()))
ans = 0
for i in range(n):
    a = input().strip()
    c = [True] * (k + 1)
    for j in a:
        if j <= str(k):
            c[int(j)] = False
    if c.count(True) == 0:
        ans += 1
print(ans)
