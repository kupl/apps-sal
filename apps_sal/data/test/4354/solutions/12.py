(n, m) = map(int, input().split())
s_pos = []
c_pos = []
for i in range(n):
    (a, b) = map(int, input().split())
    s_pos.append([a, b])
for i in range(m):
    (c, d) = map(int, input().split())
    c_pos.append([c, d])
for i in range(n):
    min_dist = 10 ** 16
    c_index = 0
    for j in range(m):
        dist = abs(s_pos[i][0] - c_pos[j][0]) + abs(s_pos[i][1] - c_pos[j][1])
        if dist < min_dist:
            min_dist = dist
            c_index = j + 1
    print(c_index)
