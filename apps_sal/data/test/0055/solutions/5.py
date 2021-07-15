n, k = map(int, input().split())
c = [0] * 200010
k -= c.count(1)

for i in range(64):
    if (n >> i) & 1:
        k -= 1
        c[i] = 1

if k < 0:
    print('No')
else:
    print('Yes')

    for i in range(64, -64, -1):
        if k >= c[i]:
            c[i - 1] += c[i] * 2
            k -= c[i]
            c[i] = 0
        else:
            break

    for i in range(-64, 64):
        if c[i]:
            while k:
                c[i] -= 1
                c[i - 1] += 2
                i -= 1
                k -= 1
            break

    for i in range(64, -100010, -1):
        print('{} '.format(i) * c[i], end='')

