def main():
    q = int(input())
    old = []
    new = []
    for _ in range(q):
        a, b = list(input().split())
        flag = 1
        for i in range(len(new)):
            if new[i] == a:
                new[i] = b
                flag = 0
                break
        if flag == 1:
            old.append(a)
            new.append(b)
    n = len(old)
    print(n)
    for i in range(n):
        print(old[i], new[i])


def __starting_point():
    main()


__starting_point()
