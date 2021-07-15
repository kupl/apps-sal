import math, collections, sys
input = sys.stdin.readline
def solve():
    n=int(input())
    a = list(map(int, input().split()))
    b= list(map(int, input().split()))
    a.sort()
    b.sort()
    print(*a)
    print(*b)
for _ in range(int(input())):
    solve()
