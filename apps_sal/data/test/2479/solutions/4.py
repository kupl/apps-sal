from bisect import bisect_right

n, q = map(int, input().split())

v_lay = [(-(n - 1), n - 2)]
h_lay = [(-(n - 1), n - 2)]

ans = (n - 2) * (n - 2)
for _ in range(q):
    case, lay_pos = map(int, input().split())

    ref_lay = (v_lay if case == 1 else h_lay)

    index = bisect_right(ref_lay, (-lay_pos, n))
    _, lay = ref_lay[index - 1]

    ans -= lay

    if index == len(ref_lay):
        ref_lay = (h_lay if case == 1 else v_lay)
        laid_pos, num = ref_lay[-1]
        if laid_pos == -(lay + 1):
            ref_lay[-1] = (-(lay + 1), min(lay_pos - 2, num))
        else:
            ref_lay.append((-(lay + 1), lay_pos - 2))

print(ans)
