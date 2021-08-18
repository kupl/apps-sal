from collections import Counter

n, m = list(map(int, input().split()))
c = list(map(int, input().split()))
k = list(map(int, input().split()))

s = sum(k)

C_orig = {i + 1: k[i] for i in range(m)}

for k in set(range(1, m + 1)):
    if C_orig[k] == 0:
        del C_orig[k]

C = Counter(c[:s])

if C == C_orig:
    print('YES')
    return

for i in range(n - s):
    C[c[i]] -= 1

    if C[c[i]] == 0:
        del C[c[i]]

    C[c[i + s]] += 1

    if C == C_orig:
        print('YES')
        return

print('NO')
