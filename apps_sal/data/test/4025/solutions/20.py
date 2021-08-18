def mp():
    return list(map(int, input().split()))


a, b, c = mp()

k = min(a // 3, b // 2, c // 2)
a -= 3 * k
b -= 2 * k
c -= 2 * k

m = 0
for i in range(7):
    d = i
    cnt = 0
    x, y, z = a, b, c
    while not(x < 0 or y < 0 or z < 0):
        if d in [0, 3, 6]:
            x -= 1
        elif d in [1, 5]:
            y -= 1
        else:
            z -= 1
        d = (d + 1) % 7
        cnt += 1
    cnt -= 1
    m = max(m, cnt)
    cnt = 0

print(7 * k + m)
