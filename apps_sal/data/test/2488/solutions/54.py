import math
import sys
from collections import deque


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)
MOD = 10 ** 9 + 7
INF = float('inf')


def main():
    (N, D, A) = list(map(int, input().split()))
    monster = [list(map(int, input().split())) for _ in range(N)]
    monster.sort(key=lambda x: x[0])
    attack = []
    for i in range(N):
        attack.append(math.ceil(monster[i][1] / A))
    acc_damage = 0
    attacked = deque([])
    answer = 0
    for i in range(N):
        x = monster[i][0]
        h = attack[i]
        while attacked and x > attacked[0][0]:
            (limit, damage) = attacked.popleft()
            acc_damage -= damage
        need = max(0, h - acc_damage)
        answer += need
        acc_damage += need
        if need:
            attacked.append((x + 2 * D, need))
    print(answer)


def __starting_point():
    main()


__starting_point()
