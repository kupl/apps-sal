import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


L = int(sys.stdin.buffer.readline())
V = L.bit_length()
ans = []
for v in range(V - 1):
    ans.append((v, v + 1, 0))
    ans.append((v, v + 1, 2 ** v))

pos = V - 2
w = 1 << L.bit_length() - 1
while pos >= 0:
    if L & (1 << pos):
        ans.append((pos, V - 1, w))
        w |= L & (1 << pos)
    pos -= 1
E = len(ans)
print((V, E))
for r in ans:
    v, u, w = r
    v += 1
    u += 1
    print((v, u, w))
