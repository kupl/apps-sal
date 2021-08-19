(n, a, b, c, t) = map(int, input().split())
tl = list(map(int, input().split()))
ans = a * n
for i in tl:
    ans += max((c - b) * (t - i), 0)
print(ans)
