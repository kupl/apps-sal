from collections import deque


def read(line):
    return [int(c) for c in line.split()]


def solve(n, lines, r1, c1, r2, c2):
    queue = deque([(r1, c1, 0)])
    visited = {}
    while queue:
        (r, c, cost) = queue.pop()
        if (r, c) not in visited:
            visited[r, c] = cost
        elif cost < visited[r, c]:
            visited[r, c] = cost
        else:
            continue
        if c2 <= lines[r - 1] + 1:
            queue.appendleft((r, c2, cost + abs(c - c2)))
        last_pos = lines[r - 1] + 1
        if c < last_pos:
            queue.appendleft((r, last_pos, cost + abs(c - last_pos)))
        if r - 1 >= 1:
            last_pos_prev = lines[r - 2] + 1
            if last_pos_prev >= c:
                queue.appendleft((r - 1, c, cost + 1))
            else:
                queue.appendleft((r - 1, last_pos_prev, cost + 1))
        if r + 1 <= n:
            last_pos_next = lines[r] + 1
            if last_pos_next >= c:
                queue.appendleft((r + 1, c, cost + 1))
            else:
                queue.appendleft((r + 1, last_pos_next, cost + 1))
    return visited[r2, c2]


def main():
    with open('input.txt') as f:
        test = f.readlines()
    (n,) = read(test[0])
    lines = read(test[1])
    (r1, c1, r2, c2) = read(test[2])
    ans = solve(n, lines, r1, c1, r2, c2)
    with open('output.txt', 'w') as f:
        f.write(str(ans))


def __starting_point():
    main()


__starting_point()
