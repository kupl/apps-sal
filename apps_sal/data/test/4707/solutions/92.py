def solve(s):
    count = 0
    if s[0] == '1':
        count += 1
    if s[1] == '1':
        count += 1
    if s[2] == '1':
        count += 1
    print(count)


def __starting_point():
    solve(input())


__starting_point()
