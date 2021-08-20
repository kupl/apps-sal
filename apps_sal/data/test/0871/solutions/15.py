(n, s) = input().split(' ')
(n, s) = (int(n), int(s))
rst = [-1, -1]
last = [0, 0]
(h, m) = input().split(' ')
(h, m) = (int(h), int(m))
if (h - last[0]) * 60 + (m - last[1]) >= s + 1:
    rst = [0, 0]
else:
    last = [h, m]
    for i in range(1, n):
        (h, m) = input().split(' ')
        (h, m) = (int(h), int(m))
        if (h - last[0]) * 60 + (m - last[1]) >= 2 * s + 2:
            rst = [last[0] + s // 60, last[1] + s % 60 + 1]
            break
        last = [h, m]
if rst == [-1, -1]:
    rst = [last[0] + s // 60, last[1] + s % 60 + 1]
if rst[1] >= 60:
    rst[0] += 1
    rst[1] -= 60
print(rst[0], rst[1])
