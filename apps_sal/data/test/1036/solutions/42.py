def main(n, k, s):
    memo = dict()

    def junken(c_left, c_right):
        if c_left == 'R':
            if c_right == 'R':
                return 'R'
            elif c_right == 'P':
                return 'P'
            else:
                return 'R'
        elif c_left == 'P':
            if c_right == 'R':
                return 'P'
            elif c_right == 'P':
                return 'P'
            else:
                return 'S'
        elif c_right == 'R':
            return 'R'
        elif c_right == 'P':
            return 'S'
        else:
            return 'S'

    def f(left, left_idx, right, right_idx):
        if memo.get((left_idx, right_idx, right - left)) is not None:
            return memo[left_idx, right_idx, right - left]
        if right - left == 1:
            return s[left_idx]
        mid = left + (right - left) // 2
        res = junken(f(left, left_idx, mid, mid % n), f(mid, mid % n, right, right_idx))
        memo[left_idx, right_idx, right - left] = res
        return res
    print(f(0, 0 % n, 1 << k, (1 << k) % n))


def __starting_point():
    nk = [int(x) for x in input().split()]
    (n, k) = (nk[0], nk[1])
    s = input()
    main(n, k, s)


__starting_point()
