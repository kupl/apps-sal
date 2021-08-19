def cuenta_uno(va):
    resp = 0
    for f in range(n):
        resp += va[f].count(1)
    return resp


# ------------------------------------------
# Programa principal
# ------------------------------------------
n, t = input().split(' ')
n, t = [int(n), int(t)]
#n, t = [3, 5]
#print(n, t)
va = [[0 for i in range(n + 1)] for i in range(n)]
ch = [0 for i in range(n + 1)]
# escribe_matriz(va)

max = 0
for i in range(n + 1):
    max += i

# ciclo de segundos virtiendo vino
c1 = 1
while c1 <= t and cuenta_uno(va) < max:
    # for c1 in range(t):
    # poner la champaña
    ch = [0 for i in range(n + 1)]
    ch[0] = 1
    i_va = 0
    while sum(ch) > 0 and i_va < n and cuenta_uno(va) <= 55:
        # poner el vino en la i_va fila de vasos
        for ct in range(n):
            va[i_va][ct] += ch[ct]
        # el vino que sobre divide en 2 y pasa a los dos vasos inmediatamente inferiores
        ch = [0 for i in range(n + 1)]
        for ct in range(n):
            if va[i_va][ct] > 1:
                ch[ct] += (va[i_va][ct] - 1) / 2
                ch[ct + 1] += (va[i_va][ct] - 1) / 2
                va[i_va][ct] = 1
        i_va += 1
    # escribe_matriz(va)
    #print ("c1 = ", c1, " i_va=", i_va, "cuenta_uno", cuenta_uno(va), " ch=", ch)
    c1 += 1
# escribe_matriz(va)
print(cuenta_uno(va))
