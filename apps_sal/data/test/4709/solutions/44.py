def iroha():
    a, op, b = list(map(str, input().split()))
    a = int(a)
    b = int(b)

    if op == "+":
        result = a + b
    else:
        result = a - b

    print(result)


def __starting_point():
    iroha()


__starting_point()
