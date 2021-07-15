import sys,math,collections,itertools,functools
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N=int(input())
a=list(map(int,input().split()))

ans = functools.reduce(math.gcd,a)
print(ans)

