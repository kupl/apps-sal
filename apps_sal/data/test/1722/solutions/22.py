n = int(input())

D = {}

for _ in range(n):
    x = input()[:1]
    if x in D:
        D[x] += 1
    else:
        D[x] = 1

T = 0
for i in D:
    m = 10000000
    for j in range(D[i]):
        m = min(m, (j * (j - 1)) // 2 + ((D[i] - j) * (D[i] - j - 1)) // 2)
    T += m

print(T)
