n, h = map(int, input().split())
a = [int(_) for _ in input().split()]
res = 1
for k in range(n):
    part = a[:k + 1]
    part.sort()
    ans, ans2 = 0, 0
    if len(part) & 1:
        for i in range(0, k + 1, 2):
            ans += part[i]
        for i in range(1, k + 1, 2):
            ans2 += part[i]
        ans2 += part[-1]
        ans = min(ans, ans2)
    else:
        for i in range(1, k + 1, 2):
            ans += part[i]
    # print(part, ans)
    if ans <= h:
        res = max(res, len(part))
    else:
        break
print(res)
