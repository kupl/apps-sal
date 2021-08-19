(n, p) = [int(i) for i in input().split()]
soma = [0 for i in range(n + 1)]
for (idx, i) in enumerate(input().split()):
    soma[idx + 1] = soma[idx] + int(i) % p
r = -float('inf')
for i in range(1, n):
    r = max(r, soma[i] % p + (soma[n] - soma[i]) % p)
print(r)
