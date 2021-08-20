def main():
    (n, d, k) = map(int, input().split())
    if n < d + 1 or (d > 1 and k == 1):
        print('NO')
        return
    edges = [(1, 2)]
    stack = []
    d2 = d / 2
    d21 = d2 + 1
    for node in range(2, d + 1):
        edges.append((node, node + 1))
        stack.append([node, d2 - abs(d21 - node), k - 2])
    next_i = d + 2
    while next_i <= n:
        if not stack:
            print('NO')
            return
        node = stack[-1]
        (i, remaining_depth, remaining_degree) = node
        if remaining_depth == 0 or remaining_degree == 0:
            stack.pop()
            continue
        node[2] -= 1
        edges.append((i, next_i))
        stack.append([next_i, remaining_depth - 1, k - 1])
        next_i += 1
    print('YES')
    print('\n'.join(('{} {}'.format(a, b) for (a, b) in edges)))


main()
