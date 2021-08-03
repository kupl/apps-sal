def bfs(a, b):
    nonlocal segment
    q = [(a, b)]
    while q:
        a, b = q.pop(0)
        x = [0, 0, -1, 1, -1, 1, -1, 1]
        y = [1, -1, 0, 0, -1, 1, 1, -1]
        for i in range(8):
            a_new, b_new = a + x[i], b + y[i]
            if (a_new, b_new) in segment and segment[(a_new, b_new)] == -1:
                segment[(a_new, b_new)] = segment[(a, b)] + 1
                q.append((a_new, b_new))


x_start, y_start, x_end, y_end = list(map(int, input().split()))
n = int(input())
segment = {}
for i in range(n):
    r, a, b = list(map(int, input().split()))
    for i in range(a, b + 1):
        segment[(r, i)] = -1
if (x_end, y_end) not in segment:
    print(-1)
    quit()
segment[(x_start, y_start)] = 0
bfs(x_start, y_start)
print(segment[(x_end, y_end)])
