N, *capas = list(map(int, open(0).read().split()))
min_capa = min(capas)
print(((N + min_capa - 1) // min_capa + 4))
