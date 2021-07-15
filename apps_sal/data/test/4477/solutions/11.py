from sys import stdin, stdout
input = stdin.readline
from collections import defaultdict as dd
import math
def geti(): return list(map(int, input().strip().split()))
def getl(): return list(map(int, input().strip().split()))
def gets(): return input()
def geta(): return int(input())
def print_s(s): stdout.write(s+'\n')

def solve():
    for _ in range(geta()):
        a=geta()
        ans=0
        ans=10*(a%10-1)
        while a:
            ans+=len(str(a))
            a//=10
        print(ans)


def __starting_point():
    solve()

__starting_point()
