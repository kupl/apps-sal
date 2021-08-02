def main():
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c3 = list(map(int, input().split()))
    for i in range(0, 101):
        for j in range(0, 101):
            for k in range(0, 101):
                flag = True
                b = []
                for l in range(3):
                    b.append(c3[l] - k)
                for l in range(3):
                    if j + b[l] != c2[l]:
                        flag = False
                        break
                for l in range(3):
                    if i + b[l] != c1[l]:
                        flag = False
                        break
                if flag:
                    print('Yes')
                    return

    print('No')


def __starting_point():
    main()


__starting_point()
