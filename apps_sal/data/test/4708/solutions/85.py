def iroha():
    n, k, price, special = [int(input()) for i in range(4)]
    result = 0
    for i in range(n):
        if i < k:
            result += price
        else:
            result += special
    print(result)

def __starting_point():
    iroha()

__starting_point()
