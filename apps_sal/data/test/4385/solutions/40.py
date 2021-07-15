import sys
inp = lambda: sys.stdin.readline()
mi = lambda: map(int, inp().split())
li = lambda: list(map(int, inp().split()))
mf = lambda: map(float,inp().split())
lf = lambda: list(map(float,inp().split()))

A = int(inp())
B = int(inp())
C = int(inp())
D = int(inp())
E = int(inp())
K = int(inp())
print("Yay!" if E - A <= K else ":(")
