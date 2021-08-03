

def get_intersection(l1, r1, l2, r2):
    if min(r1, r2) < max(l1, l2):
        return -1, -1
    else:
        return max(l1, l2), min(r1, r2)


def cumsum(ones, l, r):
    ans = ones[r]
    if l != 1:
        ans -= ones[l - 1]

    return ans


def main():

    n, q = [int(x) for x in input().split(' ')]
    cnts = [0 for i in range(n + 1)]
    pep = []

    for i in range(q):
        l, r = [int(x) for x in input().split(' ')]
        pep.append((l, r))
        cnts[l] += 1
        if r != n:
            cnts[r + 1] -= 1

    ones = [0 for i in range(n + 1)]
    twos = [0 for i in range(n + 1)]
    tot = 0

    for i in range(1, n + 1):
        cnts[i] += cnts[i - 1]
        tot += cnts[i] != 0

        if cnts[i] == 1:
            ones[i] += 1
        elif cnts[i] == 2:
            twos[i] += 1

        ones[i] += ones[i - 1]
        twos[i] += twos[i - 1]

    best = -1
    for i in range(len(pep)):
        for j in range(i + 1, len(pep)):
            cur_ans = tot - cumsum(ones, *pep[i])
            cur_ans -= cumsum(ones, *pep[j])

            l, r = get_intersection(*pep[i], *pep[j])

            if l != -1:
                cur_ans -= cumsum(twos, l, r)

            best = max(best, cur_ans)

    print(best)


def __starting_point():
    main()


__starting_point()
