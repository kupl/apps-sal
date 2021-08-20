def gcd(a, b):
    b = abs(b)
    while b != 0:
        r = a % b
        (a, b) = (b, r)
    return a


(N, M) = list(map(int, input().split()))
X = [int(a) for a in input().split()]
P = [int(a) for a in input().split()]
g = 0
for i in range(N - 1):
    g = gcd(g, X[i] - X[i + 1])
for i in range(M):
    if g % P[i] == 0:
        print('YES')
        print(X[0], i + 1)
        break
else:
    print('NO')
