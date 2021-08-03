A, B, C, X, Y = map(int, input().split())
if 2 * C <= A + B:
    price = 2 * C
else:
    price = A + B
maxN = max(X, Y)
miniN = min(X, Y)
res = miniN * price
residue = maxN - miniN
if residue == 0:
    print(res)
elif X > Y:
    res += min(residue * A, residue * 2 * C)
    print(res)
elif Y > X:
    res += min(residue * B, residue * 2 * C)
    print(res)
