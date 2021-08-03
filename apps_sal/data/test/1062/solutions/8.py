n, s, t = int(input()), input(), input()

t_dict = dict()
diffs = list()
res_i, res_j = -1, -1
res_d = 0

for i in range(n):
    if s[i] == t[i]:
        continue
    res_d += 1
    diffs.append(i)
    t_dict[t[i]] = i

perfect_swapped = False
swapped = False
for i in diffs:
    if s[i] not in t_dict:
        continue
    swapped = True
    res_i = i + 1
    j = t_dict[s[i]]
    res_j = j + 1
    if s[j] == t[i]:
        perfect_swapped = True
        break

print(res_d - (2 if perfect_swapped else 1 if swapped else 0))
print(res_i, res_j)
