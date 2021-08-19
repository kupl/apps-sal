a = str(input())
i = [0]
n = [0]
t = [0]
e = [0]
for x in a:
    x = str(x)
    if x == 'i':
        i[0] += 1
    if x == 'n':
        n[0] += 1
    if x == 't':
        t[0] += 1
    if x == 'e':
        e[0] += 1
i_m = i[0]
e_m = e[0] // 3
t_m = t[0]
n_m = 0
if n[0] >= 3:
    n[0] -= 3
    n_m += 1
    n_m += n[0] // 2
print(min(i_m, n_m, e_m, t_m))


# 1481305185129
