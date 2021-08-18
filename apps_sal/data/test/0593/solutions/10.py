n, m = [int(x) for x in input().split(" ")]
victorias = [0 for x in range(n)]
for i in range(m):
    puntajes = [int(x) for x in input().split(" ")]
    ganador = puntajes.index(max(puntajes))
    victorias[ganador] += 1
print(victorias.index(max(victorias)) + 1)
