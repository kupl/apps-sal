n, m = map(int, input().split())

py = []
for i in range(m):
    p, y = map(int, input().split())
    py.append([i, p, y])
cnt = [0] * (n + 1)

sorted_py = sorted(py, key=lambda x: (x[1], x[2]))
for i in range(m):
    cnt[sorted_py[i][1]] += 1
    city_id = str(sorted_py[i][1]).zfill(6) + str(cnt[sorted_py[i][1]]).zfill(6)
    sorted_py[i].append(city_id)

sorted_py = sorted(sorted_py, key=lambda x: x[0])
for i in range(m):
    print(sorted_py[i][3])
