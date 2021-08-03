n, m = list(map(int, input().split()))
ac = 0
wa = 0
cur_n = 0
cur_wa = 0
cur_ac = False
pset = []
for i in range(m):
    p, s = input().split()
    pset.append((int(p), s))
pset.sort(key=lambda x: x[0])

for j in range(m):
    if cur_n != pset[j][0]:
        cur_n = pset[j][0]
        cur_ac = False
        cur_wa = 0
    if cur_ac == False:
        if pset[j][1] == 'AC':
            ac += 1
            wa += cur_wa
            cur_ac = True
        else:
            cur_wa += 1

print(f'{ac} {wa}')
