def iroha():
    a, b, c = list(map(int, input().split()))
    
    one = b - a
    two = c - b

    if one == two:
        print("YES")
    else:
        print("NO")



def __starting_point():
    iroha()


__starting_point()
