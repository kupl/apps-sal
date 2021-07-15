n, m = list(map(int, input().split()))
city = []

for i in range(m):
    a = list(map(int, input().split()))+[i]
    city.append(a)
city.sort(key=lambda x: x[1])

count = [1 for _ in range(n)]
for k in range(m):
    city[k].append(count[city[k][0]-1])
    count[city[k][0]-1] += 1
city.sort(key=lambda x: x[2])

for i in city:
    print((str(i[0]).zfill(6)+str(i[-1]).zfill(6)))

