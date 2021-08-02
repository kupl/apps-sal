"""
652C - Враждебные пары
http://codeforces.com/problemset/problem/652/C
Предподсчитаем сначала для каждого числа x его позицию posx в перестановке. Это легко сделать за линейное время. Теперь рассмотрим некоторую враждебную пару (a, b) (можно считать, что posa < posb). Запомним для каждого числа a самую левую позицию posb такую, что (a, b) образуют враждебную пару. Обозначим эту величину za. Теперь будем идти по перестановке справа налево и поддерживать позицию rg наибольшего корректного интервала с левым концом в текущей позиции перестановки lf. Значение rg пересчитывается следующим образом: rg = min(rg, z[lf]). Соответсвенно к ответу на каждой итерации нужно прибавлять величину rg - lf + 1.
"""


def main():
    from sys import stdin
    n, m = list(map(int, input().split()))
    n += 1
    aa, pos, duo = [0] * n, [0] * n, [0] * n
    for i, a in enumerate(map(int, input().split()), 1):
        aa[i] = a
        pos[a] = i
    for s in stdin.read().splitlines():
        x, y = list(map(int, s.split()))
        px, py = pos[x], pos[y]
        if px > py:
            if duo[x] < py:
                duo[x] = py
        else:
            if duo[y] < px:
                duo[y] = px
    res = mx = 0
    for i, a in enumerate(aa):
        if mx < duo[a]:
            mx = duo[a]
        res += i - mx
    print(res)


def __starting_point():
    main()


__starting_point()
