n, k = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    prob = 1
    now = i
    while now < k:
        now = 2 * now
        prob = prob / 2
    ans += prob / n
print(ans)
