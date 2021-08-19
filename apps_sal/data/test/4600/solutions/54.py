def resolve():
    (n, m) = map(int, input().split())
    ac_list = [0] * n
    wa_count = [0] * n
    ac = 0
    wa = 0
    for _ in range(m):
        (p, s) = input().split()
        if s == 'WA' and ac_list[int(p) - 1] == 0:
            wa_count[int(p) - 1] += 1
        elif s == 'AC' and ac_list[int(p) - 1] == 0:
            ac += 1
            ac_list[int(p) - 1] = 1
    for (i, j) in zip(wa_count, ac_list):
        if j:
            wa += i
    print(f'{ac} {wa}')


resolve()
