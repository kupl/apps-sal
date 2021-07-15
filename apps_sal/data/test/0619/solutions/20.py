import sys
input = sys.stdin.readline

################################################################################

x, y, z = map(int, input().split())
r = (x+y)//z
t = x//z+y//z
print(r, min(z-x%z, z-y%z) if r != t else 0)
