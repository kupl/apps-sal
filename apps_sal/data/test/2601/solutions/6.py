#   ==========     //\\       //||     ||====//||
#       ||        //  \\        ||     ||   // ||
#       ||       //====\\       ||     ||  //  ||
#       ||      //      \\      ||     || //   ||
#   ========== //        \\  ========  ||//====||
#  code

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    b = a[:]
    b.sort()
    b = b[::-1]
    c = set(a)
    if a == b:
        if len(c) == len(a):
            print('NO')
        else:
            print('YES')
    else:
        print('YES')
    return


def main():
    t = 1
    t = int(input())
    for _ in range(t):
        solve()


def __starting_point():
    main()


__starting_point()
