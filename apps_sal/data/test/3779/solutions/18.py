
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))


def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


g = 0

for i in a:
    g = gcd(g, i)

res = set()
for i in range(0, k * g, g):
    res.add(i % k)

print(str(len(res)) + " \n" + " ".join(map(str, sorted(res))))
