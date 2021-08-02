n, k = [int(x) for x in input().split()]

L = [int(x) for x in input().split()]

D = [0] * k

for i in L:
    D[i % k] += 1

s = 0
for i in range((k + 2) // 2):
    if i == 0:
        s += 2 * (D[0] // 2)
    elif (k % 2 == 0) and (i == k // 2):
        s += 2 * (D[i] // 2)
    else:
        s += 2 * min(D[i], D[k - i])

print(s)
