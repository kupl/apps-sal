
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    s = input()

    xx = sorted((a[i], i) for i in range(n))
    oo = [-1] * n
    for i in range(n):
        oo[xx[i][1]] = i

    # print(a)
    # print(oo)

    nn = -1
    for i in range(n):
        nn = max(nn, oo[i])
        if i < nn and s[i] == '0':
            print("NO")
            break
    else:
        print("YES")


def __starting_point():
    main()


__starting_point()
