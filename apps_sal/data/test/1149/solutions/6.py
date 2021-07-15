def main():
    n = int(input())
    p, *pi = list(map(int, input().split()))
    q, *qi = list(map(int, input().split()))

    s = set(pi)
    s.update(qi)
    if len(s) != n:
        print('Oh, my keyboard!')
    else:
        print('I become the guy.')



def __starting_point():
    main()


__starting_point()
