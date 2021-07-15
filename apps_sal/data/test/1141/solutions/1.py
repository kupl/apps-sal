import sys
sys.setrecursionlimit(100000000)
# def input(): return sys.stdin.readline()[:-1]
def iin(): return int(input())
def impin(): return list(map(int, input().split()))
def irrin(): return [int(x) for x in input().split()]
def imrin(n): return [int(input()) for _ in range(n)]


n, m = impin()
s = [x for x in input()]
for _ in range(m):
    l, r, c1, c2 = input().split()
    for i in range(int(l)-1, int(r)):
        if s[i]==c1:
            s[i] = c2
print(''.join(s))

