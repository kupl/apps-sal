import math

N = int(input())
Ai = list(set(map(int, input().split(" "))))

g = Ai[0]
for i in Ai[1:]:
    g = math.gcd(g, i)
print(g)
