(n, m) = list(map(int, input().split()))
a = sorted(map(int, input().split()))
ans = 0
cur = 0
for b in a:
    if b > cur:
        ans += 1
        cur += 1
    else:
        ans += 1
print(sum(a) - (ans + max(a) - cur))
