lectura = int(input())
lista0 = [0] * (lectura + 1)
for i in range(2, lectura + 1):
    if lista0[i] == 0:
        for j in range(2 * i, lectura + 1, i):
            lista0[j] = i
    lista0[i] = i - lista0[i] + 1
conclusion = lectura
for i in range(lista0[lectura], lectura + 1):
    conclusion = min(conclusion, lista0[i])
print(conclusion)
