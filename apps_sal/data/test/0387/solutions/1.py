a, b = list(map(int, input().split()))
ans, l, n = 0, 1, a + b
while l <= n:
    g = n // l
    if a < g or b < g:
        l = (n // g) + 1
        continue
    r = n // g
    al = (a + g) // (g + 1)
    ah = a // g
    bl = (b + g) // (g + 1)
    bh = b // g
    if (al <= ah and bl <= bh):
        ans += max(0, min(r, ah + bh) - max(l, al + bl) + 1)
    l = r + 1
print(ans)
