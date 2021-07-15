def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())

M = list(map(int, input().split()))
R = list(map(int, input().split()))

G = 1
for m in M:
    G = (G * m) // gcd(G, m)

count = 0
for d in range(G):
    for i in range(len(M)):
        if d % M[i] == R[i]:
            count += 1
            break

print(count / G)

