n = int(input())
maps = {}
for i in range(n): 
    string = input()
    for j in range(len(string)):
        for a in range(0,j + 1):
            substr = string[a:j+1]
            if substr not in maps:
                maps[substr] = {'index' : i, 'count': 1}
            else:
                if i != maps[substr]['index']:
                    maps[substr]['count'] += 1
maps = sorted(maps.items(), key = lambda i: i[1]['index'])
count = 0
min_v = ''
min_count = 10
for k, value in maps:
    if count < value['index']:
        count += 1
        print(min_v)
        min_v = 'idk'
        min_count = 10
    if value['count'] == 1:
        if len(k) < min_count:
            min_count = len(k)
            min_v = k
print(min_v)
