import sys

def solve():
    n, k = map(int, input().split())
    a = [int(i) - 1 for i in input().split()]

    kinds = len(set(a))

    if kinds <= k:
        print(kinds)
        return

    books = [False] * n
    have = 0
    cost = 0

    for i, ai in enumerate(a):
        if books[ai]:
            continue
        else:
            if have < k:
                books[ai] = True
                cost += 1
                have += 1
            else:
                trash = -1
                longest = -1

                for j in range(n):
                    if books[j]:
                        if j not in a[i + 1:]:
                            trash = j
                            break

                        m = a[i + 1:].index(j)

                        if longest < m:
                            longest = m
                            trash = j

                assert trash != -1

                books[trash] = False
                books[ai] = True
                cost += 1

        # print([i for i in range(n) if books[i]])

    print(cost)

def __starting_point():
    solve()
__starting_point()
