v = [input()[2:] for i in range(4)]
l = [(len(s), s) for s in v]

min_l, min_s = min(l)[0], min(l)[1]
max_l, max_s = max(l)[0], max(l)[1]

min_ind = 0
max_ind = 0

for i in range(4):
    if i != v.index(min_s) and len(v[i]) / min_l >= 2:
        min_ind += 1
    if i != v.index(max_s) and max_l / len(v[i]) >= 2:
        max_ind += 1

if min_ind == 3 and max_ind != 3:
    print(chr(65 + v.index(min_s)))
elif max_ind == 3 and min_ind != 3:
    print(chr(65 + v.index(max_s)))
else:
    print('C')
