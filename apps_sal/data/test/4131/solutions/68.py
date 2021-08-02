n, m = list(map(int, input().split()))
cities = []

for i in range(m):
    p, y = list(map(int, input().split()))
    cities.append([p, y, i])

sorted_cities = sorted(cities, key=lambda x: (x[0], x[1]))
cnt = 1
ans = []
for i in range(m - 1):
    p_id = str(sorted_cities[i][0]).rjust(6, '0')
    c_id = str(cnt).rjust(6, '0')
    ans.append([sorted_cities[i][2], p_id + c_id])
    if sorted_cities[i][0] != sorted_cities[i + 1][0]:
        cnt = 1
    else:
        cnt += 1

p_id = str(sorted_cities[m - 1][0]).rjust(6, '0')
c_id = str(cnt).rjust(6, '0')
ans.append([sorted_cities[m - 1][2], p_id + c_id])
ans.sort()

for id in ans:
    print((id[1]))
