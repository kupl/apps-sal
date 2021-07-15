
N = int(input())

d = []
for i in range(N):
    city, score = input().split()
    d.append({'city':city,'score':int(score),'index':i+1})


sorted_d = sorted(d, key=lambda x:x['city'])

unique_city = []

for i in sorted_d:
    if i['city'] not in unique_city:
        unique_city.append(i['city'])

for city in unique_city:
    pool = [x for x in sorted_d if x['city']==city]
    sorted_pool = sorted(pool, key=lambda x:x['score'], reverse=True)
    for i in sorted_pool:
        print((i['index']))

