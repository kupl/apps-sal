from collections import Counter
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    A = [int(_) for _ in input().split()]

    cc = Counter(A)

    mc = cc.most_common()
    vm = mc[0][1]

    nb = 0
    for _, c in mc:
        if c != vm:
            break
        nb += 1

    nbc = nb * vm
    left = N - nbc
    spaces = vm - 1
    min_blank = left//spaces
    print(min_blank + nb -1)

