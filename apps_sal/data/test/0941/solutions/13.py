def main():
    (b, k) = [int(a) for a in input().split()]
    ais = [int(a) for a in input().split()]
    if b % 2 == 0:
        if ais[-1] % 2 == 1:
            print('odd')
        else:
            print('even')
    elif sum(ais) % 2 == 1:
        print('odd')
    else:
        print('even')


main()
