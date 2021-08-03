import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a, b = map(int, input().split())
koho = []
for i in range(n):
    koho.append(abs(i * k + 1 + b - 1 - a))
    koho.append(n * k - abs(i * k + 1 + b - 1 - a))
for i in range(n):
    koho.append(abs(i * k + 1 - b - 1 - a))
    koho.append(n * k - abs(i * k + 1 - b - 1 - a))
for i in range(n):
    koho.append(abs(i * k + 1 + b - 1 + a))
    koho.append(n * k - abs(i * k + 1 + b - 1 + a))
for i in range(n):
    koho.append(abs(i * k + 1 - b - 1 + a))
    koho.append(n * k - abs(i * k + 1 - b - 1 + a))
koho = set(koho)
koho = list(koho)
ans = []


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


for i in range(len(koho)):
    if koho[i] == 0:
        continue
    p = gcd(koho[i], n * k)
    ans.append(n * k // p)
print(min(ans), max(ans))
