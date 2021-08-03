n = int(input())
a_trans = [n + 1] * (n + 1)
i = 1
for ai in input().split():
    a_trans[int(ai)] = i
    i += 1
min_unt_ake_n = 1
res = []
for bi in input().split():
    atb_i = a_trans[int(bi)]
    if atb_i < min_unt_ake_n:
        res.append('0')
    else:
        nex = atb_i + 1
        res.append(nex - min_unt_ake_n)
        min_unt_ake_n = nex
print(*res)
