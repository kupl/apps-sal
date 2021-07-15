stat = []
n, r, avg = map(int, input().split(' '))
for i in range(n):
    a, b = map(int, input().split(' '))
    stat.append([a, b, r-a])

req = n * avg
curr = sum([i[0] for i in stat])
need = req - curr

stat.sort(key = lambda x: x[1])
        
curr = 0
tot = 0
while need > 0:
    if stat[curr][2] <= need:
        tot += stat[curr][2] * stat[curr][1]
        need -= stat[curr][2]
        curr += 1
    else:
        tot += stat[curr][1] * need
        need = 0
print(tot)
