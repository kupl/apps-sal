import sys
sys.setrecursionlimit(100000000)
def iin(): return int(input())
def impin(): return list(map(int, input().split()))
def irrin(): return [int(x) for x in input().split()]
def imrin(n): return [int(input()) for _ in range(n)]


s = 0
k, p = impin()
for i in range(1, k + 1):
    s = (s + i * 10**len(str(i)) + int(str(i)[::-1])) % p
print(s)
