n = int(input())
A = [int(i) for i in input().split()]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


g = A[0]

for i in A:
    g = gcd(g, i)

fct = []

for i in range(1, g + 1):
    if i * i > g:
        break
    if g % i == 0:
        fct.append(i)
        fct.append(g // i)

print(len(set(fct)))
