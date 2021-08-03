'''
Created on 2020/09/29

@author: harurun
'''
from itertools import permutations
import sys
import math
pin = sys.stdin.readline


def main():
    N = int(pin())
    d = [list(map(int, pin().split())) for _ in [0] * N]
    l = list(permutations(list(range(N))))
    k = 0
    for i in l:
        s = 0
        for j in range(N - 1):
            x = (d[i[j]][0] - d[i[j + 1]][0])**2
            y = (d[i[j]][1] - d[i[j + 1]][1])**2
            s += math.sqrt(x + y)
        k += s
    ans = k / len(l)
    print(ans)
    return


main()
