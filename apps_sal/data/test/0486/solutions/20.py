n = list(map(int, input()))

m = 1

for i, d in enumerate(reversed(n)):
    if i == 0:
        m = d
    else:
        m = max(d*m, (max(d-1, 1))*(9**i))
print(m)
