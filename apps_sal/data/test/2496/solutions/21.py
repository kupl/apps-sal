import math
n = int(input())
a = list(map(int, input().split()))
c = [0] * (10 ** 6 + 3)
for i in a:
    c[i] += 1
pairwise = True
for i in range(2, 10 ** 6 + 1):
    if sum(c[::i]) > 1:
        pairwise = False
g = 0
for i in a:
    g = math.gcd(g, i)
if g == 1:
    setwise = True
else:
    setwise = False
if pairwise == True:
    print('pairwise coprime')
elif setwise == True:
    print('setwise coprime')
else:
    print('not coprime')
