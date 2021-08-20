n = int(input())
a = [0] + list(input())
(x, y) = (0, 0)
an = 0
(ups, dwns, rts, lts) = (0, 0, 0, 0)
for i in range(n, 0, -1):
    if a[i] == 'U':
        ups += 1
    elif a[i] == 'D':
        dwns += 1
    elif a[i] == 'R':
        rts += 1
    else:
        lts += 1
    an = max(an, 2 * min(rts, lts) + 2 * min(ups, dwns))
print(an)
