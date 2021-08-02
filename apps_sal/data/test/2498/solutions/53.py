N, M = map(int, input().split())
A = list(map(int, input().split()))


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


G = A[0] / 2
for a in A[1:]:
    G *= (a / 2) / gcd(G, a // 2)
for a in A:
    if G % a == 0:
        print(0)
        return
print(int(M // G - M // G // 2))
