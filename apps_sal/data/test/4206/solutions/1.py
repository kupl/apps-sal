res_plain = 0
res_1 = -200000
res_2 = -200000
s = input()
for c in s:
    if c in '147':
        res_plain, res_1, res_2 = res_2, res_plain, res_1
    elif c in '258':
        res_plain, res_1, res_2 = res_1, res_2, res_plain
    res_plain = max(res_1, res_2, res_plain + 1)
print(res_plain)
