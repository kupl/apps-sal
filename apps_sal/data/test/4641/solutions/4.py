from sys import stdin
input = stdin.readline
(n, x) = map(int, input().split())
przyst = [0] * x
l = []
best = 0
for i in range(n):
    nju = int(input())
    przyst[nju % x] += 1
    while True:
        if przyst[best % x] != 0:
            best += 1
            przyst[(best - 1) % x] -= 1
        else:
            break
    print(best)
