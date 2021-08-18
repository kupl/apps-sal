def main():
    a, b, c = list(map(int, input().split()))
    s = [list(map(str, input()))for i in range(a)]
    cnt = 0
    count = 0
    for i in range(2**a):
        for j in range(2**b):
            cnt = 0
            for ia in range(a):
                for ib in range(b):
                    if not i & (1 << ia) and not j & (1 << ib):
                        if s[ia][ib] == '
                        cnt += 1
            if cnt == c:
                count += 1
    print(count)


def __starting_point():
    main()


__starting_point()
