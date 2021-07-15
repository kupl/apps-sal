
n, m = list(map(int, input().split()))

regions = [[] for i in range(m)]

for i in range(n):
    name, region, score = input().split()
    region = int(region)
    score = int(score)
    regions[region - 1] += [(score, name)]

for i in range(m):
    regions[i] = sorted(regions[i])


for i in range(m):
    if len(regions[i]) > 2 and \
       regions[i][-2][0] == regions[i][-3][0]:
        print("?")
    else:
        print(regions[i][-1][1] + " " + regions[i][-2][1])








