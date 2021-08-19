def intersect(seqOne, seqTwo):
    seqOne = sorted(seqOne, key=lambda x: x[0])
    seqTwo = sorted(seqTwo, key=lambda x: x[0])
    i = 0
    j = 0
    ans = []
    while i < len(seqOne) and j < len(seqTwo):
        (a, b) = seqOne[i]
        (c, d) = seqTwo[j]
        if max(a, c) < min(b, d):
            ans.append((max(a, c), min(b, d)))
        if b < d:
            i += 1
        else:
            j += 1
    return ans


def main():
    (n, m) = map(int, input().strip().split())
    orders = []
    for i in range(m):
        orders.append([int(x) for x in input().strip().split()])
    ind = [0] * (n + 1)
    for i in range(1, n + 1):
        ind[orders[0][i - 1]] = i
    subseqs = [(1, n)]
    for i in range(1, m):
        order = list(map(lambda x: ind[x], orders[i]))
        i = 0
        currSubseqs = []
        for j in range(1, n):
            if order[j] == order[j - 1] + 1:
                continue
            else:
                if j - i > 1:
                    currSubseqs.append((order[i], order[j - 1]))
                i = j
        if i != n - 1:
            currSubseqs.append((order[i], order[j]))
        subseqs = intersect(subseqs, currSubseqs)
        if len(subseqs) == 0:
            break
    ans = n
    for subseq in subseqs:
        (x, y) = subseq
        m = y - x + 1
        ans += m * (m + 1) // 2 - m
    print(ans)


def __starting_point():
    main()


__starting_point()
