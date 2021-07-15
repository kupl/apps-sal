#   ==========     //\\       //||     ||====//||
#       ||        //  \\        ||     ||   // ||
#       ||       //====\\       ||     ||  //  ||
#       ||      //      \\      ||     || //   ||
#   ========== //        \\  ========  ||//====|| 
#  code


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    last = -1
    ans = 0
    for i, v in enumerate(a):
        if v == 1:
            if last > -1:
                ans += i - last - 1
            last = i
    print(ans)

def main():
    t = 1
    t = int(input())
    for _ in range(t):
        solve()

def __starting_point():
    main()
__starting_point()
