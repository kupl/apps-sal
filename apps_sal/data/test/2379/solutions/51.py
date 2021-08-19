def main():
    (n, k, c) = map(int, input().split())
    s = input().rstrip()
    frnt = [None] * n
    back = [None] * n
    if s[0] == 'o':
        frnt[0] = [1, 0]
    else:
        frnt[0] = [0, -1 * n - 100]
    for i in range(1, n):
        if s[i] == 'o' and i - frnt[i - 1][1] - 1 >= c:
            frnt[i] = [frnt[i - 1][0] + 1, i]
        else:
            frnt[i] = [frnt[i - 1][0], frnt[i - 1][1]]
    if s[-1] == 'o':
        back[-1] = [1, n - 1]
    else:
        back[-1] = [0, 2 * n + 100]
    for i in reversed(range(n - 1)):
        if s[i] == 'o' and back[i + 1][1] - i - 1 >= c:
            back[i] = [back[i + 1][0] + 1, i]
        else:
            back[i] = [back[i + 1][0], back[i + 1][1]]
    for i in range(n):
        if s[i] == 'x':
            continue
        a = frnt[i][0] + back[i][0]
        if i == frnt[i][1]:
            a -= 1
        if i == back[i][1]:
            a -= 1
        if i != frnt[i][1] and i != back[i][1]:
            if back[i][1] - frnt[i][1] - 1 < c:
                a -= 1
        if a == k - 1:
            print(i + 1)


def __starting_point():
    main()


__starting_point()
