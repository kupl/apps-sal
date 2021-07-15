import sys
from collections import Counter
from itertools import combinations


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()

S = []
ans = 0

for i in range(n):
    s = input()[0]
    if s in ["M","A","R","C","H"]:
        S.append(s)

C = Counter(S)

for w in combinations(["M","A","R","C","H"],3):
    ans += C[w[0]]*C[w[1]]*C[w[2]]

print(ans)
