n = int(input())
bn = list(map(int, input().split()))

an = [bn[0]]


for x in range(n - 2):
    if bn[x + 1] >= bn[x]:
        an.append(bn[x])
    else:
        an.append(bn[x + 1])

an.append(bn[-1])

print(sum(an))
