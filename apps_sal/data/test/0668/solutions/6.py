def run():
    input()
    a = list(enumerate(list(map(int, input().split()))))
    a = [a[0]] + sorted(a[1:], key=lambda k: k[1], reverse=True)
    head, tail, ans = 0, 1, []
    while head < tail < len(a):
        if a[head][1] > 0:
            ans.append((a[head][0], a[tail][0]))
            a[head] = (a[head][0], a[head][1] - 1)
            tail += 1
        else:
            head += 1
    if tail == len(a):
        print(len(ans))
        for x, y in ans:
            print(x + 1, y + 1)
    else:
        print(-1)


def __starting_point():
    run()


__starting_point()
