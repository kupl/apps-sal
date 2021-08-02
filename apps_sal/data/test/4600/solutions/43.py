n, m = map(int, input().split())

lst = [[i for i in input().split()] for j in range(m)]

ac = {}
wa = {}
visited = []
for d in lst:
    if d[0] in ac.keys():
        continue
    if d[1] == "AC":
        if d[0] not in ac.keys():
            ac[d[0]] = 1
    else:
        if d[0] in wa.keys():
            wa[d[0]] += 1
        else:
            wa[d[0]] = 1

ac_count = 0
wa_count = 0

for d in ac.keys():
    ac_count += 1
    if d in wa.keys():
        wa_count += int(wa[d])
print(ac_count, wa_count)
