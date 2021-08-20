"""
Vamos resolver esse problema com programação dinâmica. Seja D(x) o conjunto dos divisores de x e dp(d, i) o tamanho
da maior subsequência boa considerando apenas os i primeiros números onde o último número escolhido tem d como divisor.
Conseguindo calcular essas duas funções, nossa solução é max(dp(d, n) ∀d).
D(x) pode ser calculado com um crivo, e toma tempo O(nlogn).
dp(d, i) pode ser calculada com a seguinte recorrência.
dp(d, i) = dp(d, i − 1) se d não divide v[i]
dp(d, i) = 1 + max(dp(g, i − 1) ∀g ∈ D(v[i])) se d divide v[i]
Criar esses dois estados usa O(n**2) memória, que podemos reduzir para O(n) observando que nunca precisamos dos
resultados do prefixo i − 2 calculando o prefixo i.
Note que só precisamos calcular os estados dp(d, i) se d divide v[i]. O que nos da uma solução O(n√n).
"""
from math import floor, sqrt


def div(x):
    primos = [1 for i in range(x + 1)]
    p = 2
    while p < x + 1:
        if primos[p] == 1:
            for i in range(p * p, x + 1, p):
                if primos[i] == 1:
                    primos[i] = p
            primos[p] = p
        p += 1
    return primos


def fat(mindiv, x):
    fat = []
    while x != 1:
        fat.append(mindiv[x])
        x //= mindiv[x]
    return set(fat)


def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    arr = input().split()
    arr = [int(x) for x in arr]
    mindiv = div(arr[-1])
    seq = [0 for i in range(arr[-1] + 1)]
    for num in arr:
        fatores = fat(mindiv, num)
        tam = 0
        for f in fatores:
            tam = max(tam, seq[f])
        for f in fatores:
            seq[f] = tam + 1
    print(max(seq))
    return


main()
