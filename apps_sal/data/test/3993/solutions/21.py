(n, m, k) = map(int, input().split())
p = list(map(int, input().split()))
p = list(map(lambda x: x - 1, p))
dis = 0
ans = 0
cnt = 1
for i in range(m - 1):
    if (p[i] - dis) // k != (p[i + 1] - dis) // k:
        dis += cnt
        ans += 1
        cnt = 1
    else:
        cnt += 1
ans += 1
print(ans)
