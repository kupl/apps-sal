N = int(input())
ti = [int(input()) for i in range(N)]


def euc_alg(val1, val2):

    if val1 == val2:
        return val1

    mod = min(val1, val2)
    divided = max(val1, val2)
    while 1:
        tmp_mod = divided % mod

        if tmp_mod == 0:
            break
        divided = mod
        mod = tmp_mod

    ret = val1 * val2 // mod

    return ret

maxti = max(ti)
# least_common_mult = max([euc_alg(maxti, t) for t in ti])

ans = ti[0]
for t in ti:
    ans = euc_alg(ans, t)

print(ans)

