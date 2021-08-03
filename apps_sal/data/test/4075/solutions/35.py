n, m = map(int, input().split())
s = [[x for x in map(int, input().split())]for _ in range(m)]
p = list(map(int, input().split()))
ans = 0
for i in range(1 << n):
    c = 1
    for j in range(m):
        t = 0
        for k in range(1, s[j][0] + 1):
            if (i >> (s[j][k] - 1)) & 1 == 1:
                t += 1
        if t % 2 != p[j]:
            c = 0
            break
    if c:
        ans += 1
print(ans)
