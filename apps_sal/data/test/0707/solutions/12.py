import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
X = list(map(int, input().split()))
P = list(map(int, input().split()))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


x = X[1] - X[0]

for i in range(1, n):
    x = gcd(x, X[i] - X[0])

for i in range(m):
    if x % P[i] == 0:
        print("YES")
        print(X[0], i + 1)
        return

print("NO")
