def ris():

    return list(map(int, input().split()))


def testCase():

    m, k = ris()

    q = 0

    a = list(ris())

    some_is_out = False

    tmp = set()

    for i in range(m - 1):

        t, r = ris()

        t -= 1

        if r == 1 and not some_is_out:

            some_is_out = True

            tmp = tmp.union(set([x for x in range(k) if a[x] <= q]))

        if t == -1:

            q += 1

        else:

            if t in tmp:

                tmp.remove(t)

            a[t] -= 1

            if a[t] < 0:

                a[t] = 0

                q += 1

    if tmp:

        q -= min([a[x] for x in tmp])

    print("".join(list(['Y' if a[x] - q <= 0 or x in tmp else 'N' for x in range(len(a))])))


for i in range(int(input())):

    input()

    testCase()
