import sys
sys.setrecursionlimit(100000000)
# def input(): return sys.stdin.readline()[:-1]
def iin(): return int(input())
def impin(): return list(map(int, input().split()))
def irrin(): return [int(x) for x in input().split()]
def imrin(n): return [int(input()) for _ in range(n)]


n = iin()
arr = irrin()
sa = sum(arr)
mn = 100000000
for i in range(n):
    for j in range(i, n + 1):
        s = sum(arr[i:j])
        # print(s)
        k = sa - s
        mn = min(mn, abs(s - k))
print(mn)
