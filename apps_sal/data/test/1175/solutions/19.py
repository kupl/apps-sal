LARGE = 10 ** 9 + 7


def f(pos, flag_x, flag_y, flag_z, memo, left, right):
    if pos == -1:
        return 1
    if memo[pos][flag_x][flag_y][flag_z] != -1:
        return memo[pos][flag_x][flag_y][flag_z]
    ret = 0
    if flag_x or left[pos] == '0':
        ret += f(pos - 1, flag_x, 1 if right[pos] == '1' else flag_y, flag_z, memo, left, right)
    if (flag_x or left[pos] == '0') and (flag_y or right[pos] == '1') and flag_z:
        ret += f(pos - 1, flag_x, flag_y, flag_z, memo, left, right)
    if flag_y or right[pos] == '1':
        ret += f(pos - 1, 1 if left[pos] == '0' else flag_x, flag_y, 1, memo, left, right)
    ret %= LARGE
    memo[pos][flag_x][flag_y][flag_z] = ret
    return ret


def solve_greed_f(L, R):
    res_g = 0
    for i in range(L, R + 1):
        for j in range(i, R + 1):
            if j % i == j ^ i:
                res_g += 1
    return res_g


def main():
    (ll, rr) = list(map(int, input().split()))
    left = '{:060b}'.format(ll)[::-1]
    right = '{:060b}'.format(rr)[::-1]
    memo = [[[[-1 for m in range(2)] for k in range(2)] for j in range(2)] for i in range(60)]
    res = f(59, 0, 0, 0, memo, left, right)
    print(res)


def __starting_point():
    main()


__starting_point()
