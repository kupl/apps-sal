i = int(input())
rat = list(map(int, input().split(' ')))
ratp = sorted(list(range(i)), key=lambda x: rat[x])
final = [-1] * i

start = 0
for i in ratp:
    if start + 1 >= rat[i]:
        start = start + 1
    else:
        start = rat[i]
        
    final[i] = start

print(' '.join([str(x) for x in final]))

