n = int(input())
company = []
result = 0

for i in range(n):
    m = [int(x) for x in input().split(' ')]
    m.pop(0)
    company.append(m)

maxx = company[0][0]
for i in company:
    for j in i:
        if j > maxx:
            maxx = j

for i in range(n):
    if max(company[i]) < maxx:
        curent_max = max(company[i])
        for j in range(len(company[i])):
            company[i][j] += maxx - curent_max
            result += maxx - curent_max

print(result)
