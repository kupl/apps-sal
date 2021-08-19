def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    used = [False] * (n + 1)
    answer = [None] * n

    for i, (ai, bi) in enumerate(zip(a, b)):
        if ai == bi and not used[ai]:
            answer[i] = ai
            used[ai] = True

    perm = set(range(1, n + 1))
    ind = []
    for i, x in enumerate(answer):
        if x is not None:
            perm.remove(x)
        else:
            ind.append(i)

    perm = list(perm)
    if len(perm) == 1:
        answer[ind[0]] = perm[0]
        for x in answer:
            print(x, end=' ')
        return

    i, j = ind
    x, y = perm
    count = (a[i] != x) + (b[i] != x) + (a[j] != y) + (b[j] != y)
    if count == 2:
        answer[i] = x
        answer[j] = y
    else:
        answer[i] = y
        answer[j] = x

    for x in answer:
        print(x, end=' ')


def __starting_point():
    # import sys
    # sys.stdin = open('input.txt')
    main()


__starting_point()
