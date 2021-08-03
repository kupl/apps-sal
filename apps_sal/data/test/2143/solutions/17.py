n = int(input())
a = list(map(int, input().split(' ')))

sums = {}
for i in a:
    for j in a:
        if i == j:
            continue
        if i + j in sums:
            sums[i + j] += 1
        else:
            sums[i + j] = 1
print(max([sums[i] for i in list(sums.keys())]) // 2)
