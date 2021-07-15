X, Y = list(map(int, input().split()))

if (X+Y)%3 != 0 or X*2 < Y or Y*2 < X:
    print((0))
    return

n = (2*X - Y) // 3
m = (2*Y - X) // 3

P = 10 ** 9 + 7
N = 10 ** 6
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N+1):
    fact.append((fact[-1]*i)%P)
    inv.append((-inv[P%i] * (P // i)) %P)
    factinv.append((factinv[-1] * inv[-1])%P)
print((fact[n+m]*factinv[n]*factinv[m]%P))

