def spruce():
    n = int(input())
    tree = dict()
    parent = set()
    for i in range(n - 1):
        p = int(input())
        parent.add(p)
        childs = tree.get(p, list())
        childs.append(i + 2)
        tree[p] = childs
    is_spruce = True
    for p in parent:
        childs = set(tree[p])
        leafs = childs - parent
        if len(leafs) < 3:
            is_spruce = False
            break
    if is_spruce:
        print('Yes')
    else:
        print('No')


def __starting_point():
    spruce()


__starting_point()
