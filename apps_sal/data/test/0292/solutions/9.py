h, n = list(map(int, input().split()))
l = 1
r = 2**h
ans = 0
now = 'l'
for i in range(h, 0, -1):
    if n < (l + r) / 2 and now == 'l':
        now = 'r'
        r -= 2**(i - 1)
        ans += 1
    elif n < (l + r) / 2 and now == 'r':
        r -= 2**(i - 1)
        ans += 2**i
    elif n > (l + r) / 2 and now == 'l':
        l += 2**(i - 1)
        ans += 2**i
    else:
        now = 'l'
        l += 2**(i - 1)
        ans += 1
print(ans)
