def main():
    t, sx, sy, ex, ey = list(map(int, input().split()))
    nlt = input()
    lst = list(nlt)
    cnt = 0
    fl = False
    for i in range(len(lst)):
        if lst[i] == 'N' and sy < ey:
            sy += 1
        elif lst[i] == 'S' and sy > ey:
            sy -= 1
        elif lst[i] == 'E' and sx < ex:
            sx += 1
        elif lst[i] == 'W' and sx > ex:
            sx -= 1
        cnt += 1
        if sx == ex and sy == ey:
            fl = True
            break
    if fl:
        print(cnt)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
