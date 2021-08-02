a, b, c, d = list(map(int, input().split()))

all_prod = []

for x in [a, b]:
    for y in [c, d]:
        all_prod.append(x * y)

print((max(all_prod)))
