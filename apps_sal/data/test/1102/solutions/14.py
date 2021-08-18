
n, l = (int(i) for i in input().split())
n_criminals = [int(i) for i in input().split()]
total = 0

for i in range(101):
    cities = set([l + i, l - i])
    cities = {c for c in cities if c > 0 and c <= n}
    criminals = sum(n_criminals[c - 1] for c in cities)

    if criminals == len(cities):
        total += criminals

print(total)
