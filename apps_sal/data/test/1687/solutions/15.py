from fractions import gcd


def findGcd(data):
    g = data[0]
    for i in range(len(data) - 1):
        g = gcd(g, data[i + 1])
    return g


n = int(input())
a = [int(i) for i in input().split()]
gc = findGcd(a)
if gc in a:
    print(gc)
else:
    print(-1)
