from itertools import combinations, permutations
from collections import defaultdict


def zeror():
    return 0


def solution(n, c, cw, w):
    c.sort(key=lambda tup: tup[0])
    for (k, v) in cw.items():
        cw[k] = sorted(v, key=lambda tup: tup[0])[::-1]
    ans = []
    for elem in w:
        if elem not in cw:
            print('NO')
            return
        else:
            ans.append(cw[elem].pop())
    temp = ans[0]
    for elem in ans[1:]:
        if temp[0] >= elem[0] and temp[1] >= elem[1]:
            print('NO')
            return
        temp = elem
    print('YES')
    for elem in ans:
        print(elem[0], elem[1])


def main():
    n = int(input())
    coordinates = []
    coor_weights = defaultdict(list)
    for _ in range(n):
        coordinates.append(tuple(map(int, input().strip().split())))
        coor_weights[coordinates[-1][1] - coordinates[-1][0]].append((coordinates[-1][0], coordinates[-1][1]))
    weigths = list(map(int, input().strip().split()))
    solution(n, coordinates, coor_weights, weigths)


def __starting_point():
    main()


'\n\n5\n2 0\n0 0\n1 0\n1 1\n0 1\n0 -1 -2 1 \n\n\n'
__starting_point()
