import sys
3


def input():
    return sys.stdin.readline().strip()


for _ in range(int(input())):
    (n, m) = [int(x) for x in input().split()]
    tiles = [[[int(x) for x in input().split()] for _ in range(2)] for i in range(n)]
    print('YES' if m % 2 == 0 and any((tile[0][1] == tile[1][0] for tile in tiles)) else 'NO')
