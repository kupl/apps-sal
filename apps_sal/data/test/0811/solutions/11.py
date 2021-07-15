import sys

sys.setrecursionlimit(280000)
a, b = map(int, input().split())
ans = 0
dead = a
while a>=b:
    ans += a - a % b
    dx = a-a%b
    a-= dx
    a+= dx//b
print(ans+a)
