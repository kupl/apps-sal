import sys
import math

A, B, C, D = map(int, sys.stdin.readline().split())
lcm = C * D // math.gcd(C, D)

bc = B // C
bd = B // D
bg = B // lcm
ac = (A-1) // C
ad = (A-1) // D
ag = (A-1) // lcm

print(B - A + 1 - (bc - ac) - (bd - ad) + (bg - ag))
