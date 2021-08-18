
def cmb(n, r):
    """組み合わせ"""
    import math
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def solve(N, M, A):
    A_sum = [0]
    A_sum_mod_map = {0: 1}
    for a in A:
        A_sum.append(A_sum[-1] + a)
        tmp1 = A_sum[-1] % M
        A_sum_mod_map.setdefault(tmp1, 0)
        A_sum_mod_map[tmp1] += 1
    ans = 0
    for v in list(A_sum_mod_map.values()):
        ans += cmb(v, 2)
    print(ans)


def __starting_point():
    N, M = list(map(int, input().split()))
    A = [int(i) for i in input().split()]
    solve(N, M, A)


__starting_point()
