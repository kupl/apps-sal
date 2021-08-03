n = input()

x = list(map(int, input().split()))

x.sort()


def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


g = x[1] - x[0]

for i in range(2, len(x)):
    g = gcd(g, x[i] - x[i - 1])

acc = 0

for i in range(1, len(x)):
    acc = acc + (x[i] - x[i - 1]) / g - 1

print(int(acc))
