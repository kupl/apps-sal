import math
import collections
import sys
input = sys.stdin.readline


def case():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n] - a[n - 1])


for _ in range(int(input())):
    case()
