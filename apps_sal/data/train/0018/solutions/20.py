import random
import math
def LI(): return list(map(int, input().split()))
def MI(): return map(int, input().split())
def yes(): return print("Yes")
def no(): return print("No")
def I(): return list(input())
def J(x): return "".join(x)
def II(): return int(input())
def SI(): return input()


# ---khan17---template
t = II()
for q in range(t):
    n = II()
    R = 1 / (2 * math.sin(math.pi / (2 * n)))
    r = math.sqrt(R**2 - 0.25)
    print(2 * r)
