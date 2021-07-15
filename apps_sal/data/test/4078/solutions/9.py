def __starting_point():
    n, subset = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))
    f = []
    t = []

    for i in range(subset):
        x, y = map(int, input().split(" "))
        f.append(x - 1)
        t.append(y - 1)

    diff = 0
    answer = []

    for ma in range(n):
        for mi in range(n):
            inside = 0
            cur_answer = []
            for sub in range(subset):
                if f[sub] <= mi <= t[sub] and not (f[sub] <= ma <= t[sub]):
                    inside += 1
                    cur_answer.append(sub)
            if a[ma] - (a[mi] - inside) > diff:
                diff = a[ma] - (a[mi] - inside)
                answer = cur_answer

    print(diff)
    print(len(answer))
    print(' '.join(str(x + 1) for x in answer))
__starting_point()
