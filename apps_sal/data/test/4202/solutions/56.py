(l, r) = map(int, input().split())
ans = 2019
if r - l <= 2021:
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            a = i % 2019 * (j % 2019) % 2019
            ans = min(a, ans)
    print(ans)
else:
    for p in range(l, l + 2021):
        for q in range(p + 1, l + 2022):
            b = p % 2019 * (q % 2019) % 2019
            ans = min(b, ans)
    print(ans)
