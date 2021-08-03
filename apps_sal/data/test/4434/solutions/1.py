import sys
input = sys.stdin.readline
def rInt(): return int(input())
def mInt(): return list(map(int, input().split()))
def rLis(): return list(map(int, input().split()))


t = rInt()
for _ in range(t):
    n = rInt()
    center = n // 2
    out = 0
    for i in range(1, n // 2 + 1):
        out += i * i * 8
    print(out)
