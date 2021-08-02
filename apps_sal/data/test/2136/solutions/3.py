def main():
    n = int(input())
    lst = []
    for i in range(n):
        line = input()
        lst.append(line)
    top_left = lst[0][1]
    top_right = lst[1][0]
    bot_left = lst[n - 1][n - 2]
    bot_right = lst[n - 2][n - 1]
    if top_left == top_right:
        if bot_left == bot_right and bot_left == top_left:
            print(2)
        elif bot_left != bot_right:
            print(1)
        else:
            print(0)
        if bot_left == top_left:
            print(n, n - 1)
        if bot_right == top_right:
            print(n - 1, n)
    elif bot_left == bot_right:
        print(1)
        if bot_left == top_left:
            print(1, 2)
        if bot_right == top_right:
            print(2, 1)
    else:
        print(2)
        print(2, 1)
        if bot_left == top_left:
            print(n, n - 1)
        else:
            print(n - 1, n)


def __starting_point():
    t = int(input())
    for i in range(t):
        main()


__starting_point()
