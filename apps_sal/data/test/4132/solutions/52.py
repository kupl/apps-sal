import bisect,collections,copy,itertools,math,string
import sys
from functools import reduce
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    from functools import reduce
    def gcd(*numbers):
        return reduce(math.gcd, numbers)
    n = I()
    lst = LI()
    ans = gcd(*lst)
    print(ans)
main()            

