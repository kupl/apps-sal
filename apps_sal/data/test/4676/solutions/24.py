def main():
    O = list(input())
    E = list(input())
    O.reverse()
    E.reverse()
    ans = ''
    for _ in range(200):
        ans += O.pop()
        if len(E) == 0:
            break
        ans += E.pop()
        if len(O) == 0:
            break
    print(ans)


def __starting_point():
    main()


__starting_point()
