n = int(input())
s = list(input())
r = -1
l = n
root = []


def find_right(node):
    nonlocal l, r, s, n
    while n:
        r += 1
        n -= 1
        if s[r] == '(':
            node[2].append([r, -1, []])
            find_right(node[2][-1])
        else:
            node[1] = r
            return True
    return False


def find_left(node):
    nonlocal l, r, s, n
    while n:
        l -= 1
        n -= 1
        if s[l] == ')':
            node[2].append([-1, l, []])
            find_left(node[2][-1])
        else:
            node[0] = l
            return True
    return False


is_correct = True
while n:
    r += 1
    n -= 1
    if s[r] == '(':
        root.append([r, -1, []])
        is_correct &= find_right(root[-1])
    else:
        root = [[-1, r, root]]
        is_correct &= find_left(root[-1])

sol = [[0, 1, 1]]
if is_correct:
    sol.append([len(root), 1, 1])
    for child in root:
        sol.append([len(child[2]) + 1, child[0] + 1, child[1] + 1])
        for gr_child in child[2]:
            if len(gr_child[2]):
                sol.append([len(root) + len(gr_child[2]) + 1, gr_child[0] + 1, gr_child[1] + 1])

print('%d\n%d %d' % tuple(max(sol)))
