(k, n, s, p) = map(int, input().split())
q = n // s
if n % s:
    q += 1
q *= k
w = q // p
if q % p:
    w += 1
print(w)
