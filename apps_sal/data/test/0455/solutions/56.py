n, *t = map(int, open(0).read().split())
*z, = zip(t[::2], t[1::2])
s = set((a + b) % 2for a, b in z)
if len(s) > 1:
    print(-1)
    return
s, *_ = s
d = [2**(38 - i)for i in range(39)] + [1] * (s < 1)
print(len(d))
print(*d)
for a, b in z:
    x = y = 0
    for i in d:
        if abs(a - x) > abs(b - y):
            if a - x > 0:
                print('R', end='')
                x += i
            else:
                print('L', end='')
                x -= i
        else:
            if b - y > 0:
                print('U', end='')
                y += i
            else:
                print('D', end='')
                y -= i
    print()
