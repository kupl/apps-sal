

def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    s = input()

    ret = p1 = 0
    while p1 < n:
        p2, temp = p1, []
        while p2 < n and s[p2] == s[p1]:
            temp.append(a[p2])
            p2 += 1

        temp.sort(reverse=True)
        ret += sum(temp[:k])
        p1 = p2

    print(ret)


def __starting_point():
    main()


__starting_point()
