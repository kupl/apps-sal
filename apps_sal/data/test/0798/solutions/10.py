def solve(a, b, c):
    # min of all 3
    # find all combinations
    # check equality
    for i in range(a + 1):
        if b >= i and (c + i) >= a and (b - i) == (c - a + i):
            print(i, b - i, a - i)
            return
    print('Impossible')


a, b, c = list(map(int, input().split(' ')))
solve(a, b, c)
