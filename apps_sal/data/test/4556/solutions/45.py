def iroha():
    head, string, heel = list(map(str, input().split()))
    headC = head[0]
    Capital = string[0]
    heelC = heel[0]
    print((headC + Capital + heelC))

def __starting_point():
    iroha()


__starting_point()
