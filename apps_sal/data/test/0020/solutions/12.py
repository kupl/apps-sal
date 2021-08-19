def b(h, m):
    s = '%02d:%02d' % (h, m)
    return s == s[::-1]


(h, m) = list(map(int, input().split(':')))
ans = 0
while not b(h, m):
    ans += 1
    m += 1
    if m == 60:
        m = 0
        h = (h + 1) % 24
print(ans)
