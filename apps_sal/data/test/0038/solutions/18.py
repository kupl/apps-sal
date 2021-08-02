n, L = map(int, input().split())

Kef = list(map(int, input().split()))
Sas = list(map(int, input().split()))

dKef = [Kef[i + 1] - Kef[i] for i in range(n - 1)]
dKef.append(L - Kef[n - 1] + Kef[0])

dSas = [Sas[i + 1] - Sas[i] for i in range(n - 1)]
dSas.append(L - Sas[n - 1] + Sas[0])

if ' '.join(map(str, dKef)) in ' '.join(map(str, dSas * 2)):
    print("YES")
else:
    print("NO")
