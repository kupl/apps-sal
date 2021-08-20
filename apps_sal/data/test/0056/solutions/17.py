def cuenta_uno(va):
    resp = 0
    for f in range(n):
        resp += va[f].count(1)
    return resp


(n, t) = input().split(' ')
(n, t) = [int(n), int(t)]
va = [[0 for i in range(n + 1)] for i in range(n)]
ch = [0 for i in range(n + 1)]
max = 0
for i in range(n + 1):
    max += i
c1 = 1
while c1 <= t and cuenta_uno(va) < max:
    ch = [0 for i in range(n + 1)]
    ch[0] = 1
    i_va = 0
    while sum(ch) > 0 and i_va < n and (cuenta_uno(va) <= 55):
        for ct in range(n):
            va[i_va][ct] += ch[ct]
        ch = [0 for i in range(n + 1)]
        for ct in range(n):
            if va[i_va][ct] > 1:
                ch[ct] += (va[i_va][ct] - 1) / 2
                ch[ct + 1] += (va[i_va][ct] - 1) / 2
                va[i_va][ct] = 1
        i_va += 1
    c1 += 1
print(cuenta_uno(va))
