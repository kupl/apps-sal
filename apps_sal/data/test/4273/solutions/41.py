import sys
from collections import Counter
from itertools import combinations


def inint(): return int(sys.stdin.readline())
def inintm(): return map(int, sys.stdin.readline().split())
def inintl(): return list(inintm())
def instrm(): return map(str, sys.stdin.readline().split())
def instrl(): return list(instrm())


n = inint()

S = []
ans = 0

for i in range(n):
    s = input()[0]
    if s in ["M", "A", "R", "C", "H"]:
        S.append(s)

C = Counter(S)

for w in combinations(["M", "A", "R", "C", "H"], 3):
    ans += C[w[0]] * C[w[1]] * C[w[2]]

print(ans)
