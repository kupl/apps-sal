def main() -> None:
    n = input()
    if n[-1] in ['2', '4', '5', '7', '9']:
        print('hon')
    elif n[-1] in ['0', '1', '6', '8']:
        print('pon')
    else:
        print('bon')
    return


def __starting_point():
    main()


__starting_point()
