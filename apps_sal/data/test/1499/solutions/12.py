s = input().split()
n = int(s[0])
m = int(s[1])
bus = [0 for i in range(0, 4 * n)]
u = 1
i = 0
while u < m and i < n:
    bus[4 * i] = u
    bus[4 * i + 3] = u + 1
    u = u + 2
    i = i + 1
if u == m and i < n:
    bus[4 * i] = u
    u = u + 1
i = 0
while u < m and i < n:
    bus[4 * i + 1] = u
    bus[4 * i + 2] = u + 1
    u = u + 2
    i += 1
if u == m and i < n:
    bus[4 * i + 1] = u
    u = u + 1
for y in range(n):
    if bus[4 * y + 1] != 0:
        print(bus[4 * y + 1], end=' ')
    if bus[4 * y] != 0:
        print(bus[4 * y], end=' ')
    if bus[4 * y + 2] != 0:
        print(bus[4 * y + 2], end=' ')
    if bus[4 * y + 3] != 0:
        print(bus[4 * y + 3], end=' ')
