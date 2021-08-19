from sys import stdin
from heapq import heappush, heappop


def main():
    inp = stdin
    numero = inp.readline()
    while numero != '':
        numero = int(numero.strip())
        juego = inp.readline().strip().split()
        print(solucion(juego))
        numero = inp.readline()


def solucion(Arreglo):
    juego = []
    for i in range(len(Arreglo)):
        heappush(juego, int(Arreglo[i]))
    total = sum(juego)
    contador = 0
    while juego:
        contador += total
        ultimo = heappop(juego)
        contador += ultimo
        total -= ultimo
    contador -= ultimo
    return contador


main()
