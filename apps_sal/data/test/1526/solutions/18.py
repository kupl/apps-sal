line = list(map(int, input().split(' ')))
line.sort()
min_n = line[0]
mid_n = line[1]
max_n = line[2]

res = 0
res = res + max_n - mid_n
res = res + int((mid_n - min_n) / 2)
if (mid_n - min_n) & 1:
    res = res + 2
print(res)
