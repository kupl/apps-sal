import queue
h, w = list(map(int, input().split()))
s = []
black_num = 0
for i in range(h):
    s_ij = input()
    s.append(s_ij)
    for j in range(w):
        if s_ij[j] == "#":
            black_num += 1

already_pass = set()
already_pass.add((1, 1))
q = queue.Queue()
q.put([(1, 1), 1])

while not q.empty():
    x_y, l = q.get()
    x = x_y[0]
    y = x_y[1]
    if x == h and y == w:
        print((h * w - black_num - l))
        break
    next_xy = [(max(1, x - 1), y), (min(h, x + 1), y),
               (x, max(1, y - 1)), (x, min(w, y + 1))]
    for i in next_xy:
        if i not in already_pass and s[i[0] - 1][i[1] - 1] != "#":
            q.put([i, l + 1])
            already_pass.add(i)
else:
    print((-1))

