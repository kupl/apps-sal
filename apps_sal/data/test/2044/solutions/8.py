cur = 0
n, m = list(map(int, input().split()))
ans = []
for a in map(int, input().split()):
    cur += a
    ans += [cur // m]
    cur %= m
print(' '.join(map(str, ans)))
