import math
def lectura(): return map(int, input().split())


x, y = lectura()
mod = 1000000007
if (y % x != 0):
    print("0")
else:
    y = y // x
    setPrueba = set()
    for i in range(1, int(math.sqrt(y) + 1)):
        if (y % i == 0):
            setPrueba.add(i)
            setPrueba.add(y // i)
    setPrueba = sorted(list(setPrueba))
    setOrdenado = setPrueba.copy()
    for i in range(len(setOrdenado)):
        setOrdenado[i] = pow(2, setPrueba[i] - 1, mod)
        for j in range(i):
            if setPrueba[i] % setPrueba[j] == 0:
                setOrdenado[i] -= setOrdenado[j]
    print(setOrdenado[len(setOrdenado) - 1] % mod)
