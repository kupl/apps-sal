import sys
sys.setrecursionlimit(10 ** 6)
(D, G) = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(D)]


def solve(bit):
    if bit >= 1 << D:
        return 1000
    p_sum = 0
    num = 0
    for i in range(D):
        if bit & 1 << i:
            p_sum += pc[i][1] + pc[i][0] * 100 * (i + 1)
            num += pc[i][0]
    if p_sum >= G:
        return min(num, solve(bit + 1))
    else:
        for i in reversed(range(D)):
            if bit & 1 << i:
                continue
            for j in range(pc[i][0]):
                if p_sum >= G:
                    break
                p_sum += 100 * (i + 1)
                num += 1
            else:
                return solve(bit + 1)
        return min(num, solve(bit + 1))


print(solve(0))
