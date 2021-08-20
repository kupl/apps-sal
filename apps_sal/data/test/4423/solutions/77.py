n = int(input())
L = []
for i in range(n):
    (s, p) = input().split()
    L.append([s, int(p), i + 1])
L.sort(key=lambda L: (L[0], -L[1]))
for l in L:
    print(l[2])
