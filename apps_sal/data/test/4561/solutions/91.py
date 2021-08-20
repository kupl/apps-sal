def LI():
    return list(map(int, input().split()))


(X, A, B) = LI()


def main():
    x = B - A
    if x <= 0:
        ans = 'delicious'
    elif x <= X:
        ans = 'safe'
    else:
        ans = 'dangerous'
    print(ans)


def __starting_point():
    main()


__starting_point()
