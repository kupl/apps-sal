def submit():
    (n, a, b) = (int(e) for e in input().split())
    h = [int(input()) for _ in range(n)]

    def judge(t):
        base_damage = b * t
        add_attack = 0
        for hi in h:
            if hi <= base_damage:
                continue
            res = hi - base_damage
            (q, r) = divmod(res, a - b)
            add_attack += q
            if r:
                add_attack += 1
        return add_attack <= t
    max_attack = 0
    for hi in h:
        max_attack += hi // a + 1
    min_attack = 0
    while True:
        mid = (min_attack + max_attack) // 2
        if mid == min_attack:
            break
        elif judge(mid):
            max_attack = mid
        else:
            min_attack = mid
    print(max_attack)


def __starting_point():
    submit()


__starting_point()
