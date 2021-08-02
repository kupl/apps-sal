def main():
    S = input()
    if S == 'RRR':
        ans = 3
    elif S in ['RRS', 'SRR']:
        ans = 2
    elif S == 'SSS':
        ans = 0
    else:
        ans = 1
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
