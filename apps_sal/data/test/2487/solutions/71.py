from collections import deque
import math


def Next(): return input()
def NextInt(): return int(Next())
def NextInts(): return map(int, input().split())
def Nexts(): return map(str, input().split())
def NextIntList(): return list(map(int, input().split()))
def RowInts(n): return [input() for i in range(n)]


n = NextInt()
ans = 0
for i in range(n):
    ans += (n - i) * (i + 1)
for i in range(n - 1):
    u, v = NextInts()
    if u > v:
        u, v = v, u
    ans -= u * (n - v + 1)
print(ans)
