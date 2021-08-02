import sys
def mapin(): return map(int, sys.stdin.readline().split())
def listin(): return list(map(int, sys.stdin.readline().split()))
def inp(): return sys.stdin.readline()


A, B, C, D = mapin()
l = A + B
r = C + D
if l < r:
    print("Right")
elif l > r:
    print("Left")
else:
    print("Balanced")
