
from collections import defaultdict


def submit():
    n, m = list(map(int, input().split()))
    a = [int(e) for e in input().split()]

    # mod mを適用
    a_mod = [e % m for e in a]
    s_mod = []
    prev = 0
    for am in a_mod:
        prev += am
        prev %= m
        s_mod.append(prev)

    mod_cnt = defaultdict(int)
    mod_cnt[0] = 1
    ans = 0
    for s in s_mod:
        ans += mod_cnt[s]
        mod_cnt[s] += 1

    print(ans)


submit()
