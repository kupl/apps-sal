def solver():
    N = int(input())
    ans = []
    for i in range(1, N + 1):
        s, p = [n for n in input().split()]
        ans.append({'id': i, 'city': s, 'point': int(p)})
    ans_s = sorted(ans, key=lambda x: (x['city'], -x['point']))
    for j in ans_s:
        print((j['id']))


def __starting_point():
    solver()


__starting_point()
