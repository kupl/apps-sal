N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]


def judge(t):
    base_damage = B * t
    add_attack = 0
    for hi in H:
        if hi <= base_damage:
            continue
        res = hi - base_damage
        q, r = divmod(res, A - B)
        add_attack += q
        if r:
            add_attack += 1
    return add_attack <= t


MAX = max(H)
max_attack = MAX // B + 1
min_attack = 0
while True:
    mid = (min_attack + max_attack) // 2
    if mid == min_attack:
        break
    else:
        if judge(mid):
            max_attack = mid
        else:
            min_attack = mid
print(max_attack)
