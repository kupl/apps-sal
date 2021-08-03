def solve(X):
    ans = 1

    for i in range(1, 32):
        for j in range(2, 11):
            tmp = i ** j
            if tmp <= X and ans < tmp:
                ans = tmp

    return ans


def __starting_point():
    X = int(input())
    print((solve(X)))


__starting_point()
