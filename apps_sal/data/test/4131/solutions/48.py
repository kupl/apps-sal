def make_code(prifacture_num, city_num):
    s1 = str(prifacture_num)
    while len(s1) != 6:
        s1 = '0' + s1
    s2 = str(city_num)
    while len(s2) != 6:
        s2 = '0' + s2
    return s1 + s2


prifacture_cnt, city_cnt = list(map(int, input().split()))
data = [list(map(int, input().split())) for i in range(city_cnt)]
city_data = []

for i in range(city_cnt):
    city_data.append([data[i][0], data[i][1], i])

city_data.sort()
city_code = []
prifacture = city_data[0][0]
cnt = 0
for city in city_data:
    if prifacture == city[0]:
        cnt+=1
        s = make_code(prifacture, cnt)
        city_code.append([city[2], s])
    else:
        cnt = 1
        prifacture = city[0]
        s = make_code(prifacture, cnt)
        city_code.append([city[2], s])

city_code.sort()
for num,code in city_code:
    print(code)

