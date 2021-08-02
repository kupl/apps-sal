n, m, k = [int(_) for _ in input().split(" ")]

p = [int(input()) for i in range(0, m + 1)]
fd = p[-1]
ans = 0
for x in iter(p[:-1]):
    t = x ^ fd
    cnt = 0
    while t:
        if t % 2 == 1:
            cnt += 1
        t = t >> 1
    if cnt <= k:
        ans += 1
print(ans)
