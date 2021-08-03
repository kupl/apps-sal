def main():
    N = int(input())
    S = input()
    stack = []
    cur = 0
    ans = N
    for c in S:
        if c == "f" and cur != 0:
            stack.append(cur)
            cur = 1
        elif c == "f" and cur == 0:
            cur += 1
        elif c == "o" and cur == 1:
            cur += 1
        elif c == "x" and cur == 2:
            ans -= 3
            if len(stack):
                cur = stack.pop()
            else:
                cur = 0
        else:
            cur = 0
            stack = []
    print(ans)


def __starting_point():
    main()


__starting_point()
