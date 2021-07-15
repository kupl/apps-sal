

def solve(l):
    helper = {
        1: {
            2: 3,
            3: 4
        },
        2: {
            1: 3,
            3: float('inf')
        },
        3: {
            1: 4,
            2: float('inf')
        }
    }
    p_i, a_i = 0, 1
    pp_i = -1
    ppre = None
    res = 0
    while a_i < len(l):
        if a_i > 1:
            pp_i += 1
            ppre = l[pp_i]
        pre, aft = l[p_i], l[a_i]
        res += helper[pre][aft]
        if res == float('inf'):
            return False, None
        if ppre is not None and (ppre, pre, aft) == (3, 1, 2):
            res -= 1
        p_i += 1
        a_i += 1
    return True, res


def __starting_point():
    _ = input()
    l = [int(x) for x in input().split()]
    is_finite, res = solve(l)
    if is_finite:
        print('Finite')
        print(res)
    else:
        print('Infinite')

__starting_point()
