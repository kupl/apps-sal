n, n1, n2 = list(map(int, input().split()))
values = sorted(map(int, input().split()), key=lambda x: -x)

if n1 > n2:
    n1, n2 = n2, n1

g1 = values[:n1]
g2 = values[n1:n1 + n2]

print(sum(g1) / n1 + sum(g2) / n2)
