
def notify(xs, xs_sorted, ind_sorted, n, answer):
    if not xs_sorted[ind_sorted][1]:
        return

    ind = xs_sorted[ind_sorted][0]

    i = 0
    while i < n and xs[ind] > 0:
        if i == ind_sorted or xs_sorted[i][1]:
            i += 1
            continue

        xs_sorted[i][1] = True
        xs[ind] -= 1
        answer.append((ind + 1, xs_sorted[i][0] + 1))
        i += 1


def main():
    n = int(input())
    xs = [int(x) for x in input().split()]
    xs_sorted = sorted(([i, i == 0, x] for (i, x) in enumerate(xs)), key=lambda x: x[2], reverse=True)

    answer = []
    f = xs_sorted.index([0, True, xs[0]])
    notify(xs, xs_sorted, f, n, answer)

    for i in range(n):
        if i != f:
            notify(xs, xs_sorted, i, n, answer)

    if all(x[1] for x in xs_sorted):
        print(len(answer))
        for a, b in answer:
            print(a, b)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
