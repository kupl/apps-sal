import sys
mapin = lambda: map(int, sys.stdin.readline().split())
listin = lambda: list(map(int, sys.stdin.readline().split()))
inp = lambda: sys.stdin.readline()
A,B,C,D = mapin()
l = A + B;r = C + D
if l < r:print("Right")
elif l > r:print("Left")
else:print("Balanced")
