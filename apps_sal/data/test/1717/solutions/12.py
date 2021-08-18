n = int(input())
d = {}
for i in range(2, 31):
    d[i] = 0

for i in range(2, n + 1):
    s = {}
    for j in range(2, 31):
        s[j] = 0
    x = i
    for j in range(2, i + 1):
        while x % j == 0 and x >= j:
            s[j] += 1
            x /= j

    for j in range(2, n + 1):
        if s[j] > d[j]:
            d[j] = s[j]

ans = int(1)
for i in range(2, n + 1):
    ans *= (i ** d[i])

print((ans + 1))
