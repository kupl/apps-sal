import bisect

def binom(n, k):
    if k > n:
        return 0
    elif k == 1:
        return n
    elif k == 2:
        return n * (n - 1) // 2
    elif k == 3:
        return n * (n - 1) * (n - 2) // 6
    else:
        assert False

def get_len(arr, a, b):
    lo = bisect.bisect_left(arr, a)
    hi = bisect.bisect_right(arr, b)
    return hi - lo

def solve(gs, ds, fs):
    ans = 0

    # min is goalkeeper, could be equal to attacker or defender if there were equal numbers
    for num_g in gs:
        ways_g = 1
        len_d = get_len(ds, num_g, num_g * 2)
        ways_d = binom(len_d, 2)
        len_f = get_len(fs, num_g, num_g * 2)
        ways_f = binom(len_f, 3)
        ways = ways_g * ways_d * ways_f
        # print(f'goalkeeper: ways={ways}, ways_gdf={ways_g, ways_d, ways_f}, num_g={num_g}')
        ans += ways

    # min is defender, could be equal to attacker if there were equal numbers
    for i, num_d in enumerate(ds[:-1]):
        ways_g = get_len(gs, num_d + 1, num_d * 2)
        ways_d = get_len(ds, num_d + 1, num_d * 2)
        len_f = get_len(fs, num_d, num_d * 2)
        ways_f = binom(len_f, 3)
        ways = ways_g * ways_d * ways_f
        # print(f'defender:   ways={ways}, ways_gdf={ways_g, ways_d, ways_f}, num_d={num_d}')
        ans += ways

    # min is attacker
    for i, num_f in enumerate(fs[:-2]):
        ways_g = get_len(gs, num_f + 1, num_f * 2)
        len_d = get_len(ds, num_f + 1, num_f * 2)
        ways_d = binom(len_d, 2)
        len_f = get_len(fs, num_f + 1, num_f * 2)
        ways_f = binom(len_f, 2)
        ways = ways_g * ways_d * ways_f
        # print(f'attacker:   ways={ways}, ways_gdf={ways_g, ways_d, ways_f}, num_f={num_f}')
        ans += ways

    return ans

_, _, _ = [int(v) for v in input().split()]
gs = [int(v) for v in input().split()]
ds = [int(v) for v in input().split()]
fs = [int(v) for v in input().split()]

gs.sort()
ds.sort()
fs.sort()

ans = solve(gs, ds, fs)
print(ans)

