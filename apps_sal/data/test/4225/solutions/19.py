import sys
def input(): return sys.stdin.readline().rstrip()

A,B,C,K = map(int,input().split())

point = 0

if A <= K:
    point += A
    K -= A
else:
    point += K
    K = 0

if B <= K:
    K -= B
else:
    K = 0

point -= K

print(point)
