def solve(level):
    level_size = len(level)

    def check(k, l):
        c = 0
        while k + l < level_size and '*' == level[k + l]:
            c += 1
            k += l
        return c >= 4

    for i in range(level_size):
        if '*' == level[i]:
            for j in range(i + 1, level_size):
                if '*' == level[j] and check(i, j - i):
                    return 'yes'
    return 'no'


input()
print(solve(input().strip()))
