def main():
    n = int(input())
    ans = [] if n != 0 else [0, ]
    while n:
        ans.append(-(n % -2))
        n = -(n // 2)
    print((''.join(list(map(str, ans[::-1])))))


def __starting_point():
    main()


__starting_point()
