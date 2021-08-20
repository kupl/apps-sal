def main():
    (n, q) = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n - 1)]
    tree = [list() for _ in range(n)]
    score = [0] * n
    for (a, b) in ab:
        (a, b) = (a - 1, b - 1)
        tree[a].append(b)
        tree[b].append(a)
    e = [0]
    while len(e) > 0:
        i = e.pop()
        for j in tree[i]:
            tree[j].remove(i)
            e.append(j)
    px = [list(map(int, input().split())) for _ in range(q)]
    for (p, x) in px:
        p -= 1
        score[p] += x
    add(tree, score)
    print(*score)


def add(tree, score):
    s = tree[0][:]
    for i in s:
        score[i] += score[0]
    while len(s) > 0:
        t = s.pop()
        for i in tree[t]:
            s.append(i)
            score[i] += score[t]


def __starting_point():
    main()


__starting_point()
