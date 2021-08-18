n = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


c = [0] * (10**6 + 3)
for i in a:
    c[i] += 1

pairwise = True
for i in range(2, 10**6 + 1):
    if sum(c[::i]) > 1:
        pairwise = False

g = 0
for i in a:
    g = gcd(g, i)
if g == 1:
    setwise = True
else:
    setwise = False

if pairwise == True:
    print("pairwise coprime")
    return
if setwise == True:
    print("setwise coprime")
    return
print("not coprime")
