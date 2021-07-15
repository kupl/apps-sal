import sys
read = sys.stdin.read
#readlines = sys.stdin.readlines
from itertools import permutations
from math import factorial
def main():
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]

    # 町同士の距離をxydisにいれる
    xydis = [[0] * n for _ in range(n)]
    for i1 in range(n):
        for i2 in range(n):
            xydis[i1][i2] = ((xy[i1][0] - xy[i2][0])**2 + (xy[i1][1] - xy[i2][1])**2)**0.5
    # 組み合わせごとの距離をdis_sumに足す。
    per = tuple(permutations(range(n), n))
    dis_sum = 0
    for pere in per:
        for j1 in range(n - 1):
            dis_sum += xydis[pere[j1]][pere[j1 + 1]]
    ans = dis_sum / factorial(n)
    print(ans)

def __starting_point():
    main()
__starting_point()
