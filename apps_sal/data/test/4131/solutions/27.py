N, M = map(int, input().split())

p_dict = {}

for i in range(M):
    p, y = map(int, input().split())
    if p not in p_dict.keys():
        p_dict[p] = [[y, p, i]]
    else:
        p_dict[p].append([y, p, i])

ans = []
for p in p_dict.keys():
    p_dict[p].sort()
    for i in range(len(p_dict[p])):
        p_dict[p][i].append(i + 1)
        ans.append(p_dict[p][i])

ans.sort(key=lambda x: x[2])
for y, p, oi, si in ans:
    print("{:06d}{:06d}".format(p, si))
