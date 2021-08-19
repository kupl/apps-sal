from sys import stdin, stdout


def solve(c, n):
    c = list(sorted(c))
    root = Root()
    root.value = c.pop()
    left_bound = root
    right_bound = root
    while len(c) > 0:
        val = c.pop()
        node = Node()
        node.value = val
        if left_bound.value > val:
            node.prev = left_bound
            if left_bound == root:
                root.left = node
            else:
                left_bound.next = node
            left_bound = node
        elif right_bound.value > val:
            node.prev = right_bound
            if right_bound == root:
                root.right = node
            else:
                right_bound.next = node
            right_bound = node
    res_len = 0
    res_str = ''
    p = left_bound
    while p is not root:
        res_str += str(p.value) + ' '
        res_len += 1
        p = p.prev
    res_str += str(p.value) + ' '
    res_len += 1
    p = root.right
    while p is not None:
        res_str += str(p.value) + ' '
        res_len += 1
        p = p.next
    return (res_len, res_str)


class Node:
    value = None
    next = None
    prev = None


class Root:
    value = None
    right = None
    left = None


def __starting_point():
    n_s = stdin.readline()
    cards_s = stdin.readline().split(' ')
    n = int(n_s)
    cards = [int(c) for c in cards_s]
    root = solve(cards, n)
    print('{}\n{}'.format(root[0], root[1]))


__starting_point()
