import math


n, m = list(map(int, input().split()))
x = input().split()
x = [int(xi) for xi in x]
p = input().split()
p = [int(pi) for pi in p]

gcds = x[1] - x[0]
for i in range(2, n):
    gcds = math.gcd(gcds, x[i] - x[i - 1])

for i in range(m):
    if gcds % p[i] == 0:
        print("YES")
        print(x[0], i + 1)
        return
print("NO")

