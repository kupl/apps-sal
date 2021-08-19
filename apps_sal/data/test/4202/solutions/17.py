(l, r) = list(map(int, input().split()))
m = ans = 2019
if l // m < r // m:
    print(0)
else:
    (a, b) = (l % m, r % m)
    for i in range(a, b + 1):
        for j in range(i + 1, b + 1):
            ans = min(ans, i * j % m)
    print(ans)
