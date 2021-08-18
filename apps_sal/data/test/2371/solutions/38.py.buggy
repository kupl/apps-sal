import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, z, w = list(map(int, input().split()))
a = list(map(int, input().split()))

last = a[-1]

if n == 1:
    print((abs(w - last)))
    return

last2 = a[-2]

print((max(abs(last2 - last), abs(last - w))))
