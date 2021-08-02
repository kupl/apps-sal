from sys import stdin


def getval():
    n = int(input())
    e = [[i] + list(map(int, stdin.readline().split())) for i in range(n - 1)]
    return n, e


def main(n, e):
    tree = [[] for i in range(n)]
    ans = [0 for i in range(n - 1)]
    for i in e:
        tree[i[1] - 1].append([i[2] - 1, i[0]])
    tree[0].append(0)
    k = 1
    q = [0]
    while q:
        n = 0
        idx = q.pop(0)
        for i in range(len(tree[idx]) - 1):
            n += 1
            if n == tree[idx][-1]:
                n += 1
            ans[tree[idx][i][-1]] = n
            tree[tree[idx][i][0]].append(n)
            q.append(tree[idx][i][0])
        k = max(k, n)

    print(k)
    for i in ans:
        print(i)


def __starting_point():
    n, e = getval()
    main(n, e)


__starting_point()
