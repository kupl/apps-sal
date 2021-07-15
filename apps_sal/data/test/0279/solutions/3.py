def solve(v1, v2, t, d):
    cache = {}

    def calc_max(cur_v, remain_t):
        if remain_t == 0:
            return 0

        cur_dist = float('-inf')
        if remain_t == 1 and cur_v != v2:
            return cur_dist

        cache_key = (cur_v, remain_t)
        if cache_key in cache:
            return cache[cache_key]

        max_v = min(cur_v + d, v2 + d*remain_t)
        min_v = max(0, max(cur_v - d, v2 - d*remain_t))
        for v in range(max_v, min_v - 1, -1):
            cur_dist = max(cur_dist, calc_max(v, remain_t - 1))

        cache[cache_key] = cur_v + cur_dist
        return cur_v + cur_dist

    return calc_max(v1, t)


def main():
    v1, v2 = list(map(int, input().strip().split()))
    t, d = list(map(int, input().strip().split()))
    print(solve(v1, v2, t, d))

main()

