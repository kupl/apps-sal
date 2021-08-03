n = list(input())
f = False
frst = -10 ** 7
for i in range(len(n)):
    if int(n[i]) % 2 == 0:
        frst = max(i, frst)
        if int(n[i]) < int(n[-1]):
            n[i], n[-1] = n[-1], n[i]
            f = True
            break
if not f and frst != -10 ** 7:
    n[frst], n[-1] = n[-1], n[frst]
    f = True
print(''.join(n) if f else '-1')
