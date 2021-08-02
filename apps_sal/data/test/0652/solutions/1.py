from collections import defaultdict
def mp(): return list(map(int, input().split()))
def lt(): return list(map(int, input().split()))
def pt(x): print(x)
def ip(): return input()
def it(): return int(input())
def sl(x): return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x): return "{0:b}".format(x)


n = it()
P = []
for i in range(n):
    a, b = mp()
    P.append([a, b])
Mid = defaultdict(int)
result = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        x, y = P[i][0] + P[j][0], P[i][1] + P[j][1]
        result += Mid[(x, y)]
        Mid[(x, y)] += 1
print(result)
