def solve():
    S = input()

    P = {
        '>': '<',
        ']': '[',
        ')': '(',
        '}': '{',
    }

    stack = []
    n = 0
    ans = 0
    for i, c in enumerate(S):
        if c in '<[{(':
            n += 1
            stack.append(c)
        else:
            n -= 1
            if len(stack) == 0:
                print('Impossible')
                return
            x = stack.pop()
            if x != P[c]:
                ans += 1

    if n != 0:
        print('Impossible')
        return

    print(ans)


def __starting_point():
    solve()

__starting_point()
