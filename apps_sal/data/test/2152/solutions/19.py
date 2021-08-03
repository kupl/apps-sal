n = int(input())
a = []
p = []

for i in range(n):
    ai, pi = list(map(int, input().split()))
    a.append(ai)
    p.append(pi)

cost = 0
meat = 0
for i in range(n):
    if meat == 0:
        cost += p[i] * a[i]
        meat += a[i]
        for j in range(i + 1, n):
            if p[j] < p[i]:
                break
            cost += p[i] * a[j]
            meat += a[j]

    meat -= a[i]

print(cost)
