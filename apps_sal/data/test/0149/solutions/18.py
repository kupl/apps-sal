x, y, l, r = list(map(int, input().split()))
degree_x = []
degree_y = []
i = 0
while x ** i <= r:
    degree_x.append(x ** i)
    i += 1
i = 0
while y ** i <= r:
    degree_y.append(y ** i)
    i += 1
sad_years = []
for i in degree_x:
    for j in degree_y:
        sad_years.append(i + j)
sad_years.sort()
res = 0
i = 0
while i < len(sad_years):
    if sad_years[i] < l or sad_years[i] > r:
        sad_years.pop(i)
    else:
        i += 1
res = 0
sad_years = [l - 1] + sad_years + [r + 1]
for i in range(len(sad_years) - 1):
    res = max(res, sad_years[i + 1] - sad_years[i] - 1)
print(res)
