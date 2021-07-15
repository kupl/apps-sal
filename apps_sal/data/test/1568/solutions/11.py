n, a, b, c, t = list(map(int, input().split()))
v = sorted(list(map(int, input().split())))

ans = 0
for i in v:
    if i > t:
        break
    if (c > b):
        ans += (t - i) * (c - b) + a
    else:
        ans += a
print(ans)


