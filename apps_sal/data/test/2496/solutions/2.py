import sys


def LI():
    return list(map(int, input().split()))


def gcd(x, y):
    if x == 0:
        return y
    else:
        return gcd(y % x, x)


input()
A = LI()

g = 0
for a in A:
    g = gcd(g, a)
if g != 1:
    print("not coprime")
    return

sosudayo = [True] * 1100000
sosudayo[0] = False
sosudayo[1] = False
for i in range(2, 1100000):
    if not sosudayo[i]:
        continue
    for j in range(i * i, 1100000, i):
        sosudayo[j] = False

used = [False] * 1100000
sosu = [a for a in A if sosudayo[a]]
for i in sosu:
    used[i] = True
ruto_sosu = [a for a in range(1100) if sosudayo[a]]
not_sosu = [a for a in A if not sosudayo[a]]

for i in not_sosu:
    for j in ruto_sosu:
        if i == 1:
            break
        if i % j != 0:
            continue
        if used[j]:
            print("setwise coprime")
            return
        used[j] = True
        while i % j == 0:
            i //= j
    if i > 1:
        if used[i]:
            print("setwise coprime")
            return
        used[i] = True

print("pairwise coprime")
