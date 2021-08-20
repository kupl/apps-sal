import math


def gns():
    return list(map(int, input().split()))


n = int(input())
ns = []


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


for i in range(n):
    ns.append(gns())
a1 = ns[0][1]
a2 = ns[0][2]
g = gcd(a1, a2)
a1 = a1 // g
a2 = a2 // g
a12 = ns[1][2]
x = int(math.sqrt(a12 // a1 // a2))
for y in range(x - 1, x + 2):
    if y * y * a1 * a2 == a12:
        break
a1 = y * a1
ans = [None] * n
ans[1] = a1
for i in range(n):
    if i == 1:
        continue
    ans[i] = ns[1][i] // a1
print(' '.join(map(str, ans)))
