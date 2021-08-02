from collections import Counter
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
EDGE = [list(map(int, input().split())) for i in range(n - 1)]
mod = 10**9 + 7

Group = [i for i in range(n + 1)]


def find(x):
    while Group[x] != x:
        x = Group[x]
    return x


def Union(x, y):
    if find(x) != find(y):
        Group[find(y)] = Group[find(x)] = min(find(y), find(x))


for x, y, c in EDGE:
    if c == 0:
        Union(x, y)

G = [find(i) for i in range(1, n + 1)]

counter = Counter(G)

ANS = 0
for j in list(counter.values()):
    ANS = (ANS + pow(j, k, mod)) % mod

print((pow(n, k, mod) - ANS) % mod)
