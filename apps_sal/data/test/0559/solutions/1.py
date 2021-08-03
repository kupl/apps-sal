import numpy as np

p = int(input())
aaa = list(map(int, input().split()))

bins = [1]
for i in range(1, p):
    bins.append(bins[-1] * (p - i) * pow(i, p - 2, p) % p)
bins = np.array(bins, dtype=np.int32)

pows_base = -np.arange(p, dtype=np.int32)
pows = np.zeros((p, p), dtype=np.int32)
pows[:, p - 1] = 1
for i in range(p - 2, -1, -1):
    pows[:, i] = pows[:, i + 1] * pows_base % p

coefs = np.zeros(p, dtype=np.int32)

for i, a in enumerate(aaa):
    if a == 0:
        continue

    coefs[0] += 1
    coefs = (coefs - bins * pows[i]) % p

print((*coefs))
