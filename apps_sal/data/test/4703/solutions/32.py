s = input()
all_s = []


def ss(index, perm):
    if index == len(s):
        all_s.append(perm)
    else:
        perm1 = [i for i in perm]
        perm1[-1] += s[index]
        ss(index + 1, perm1)

        perm2 = [i for i in perm]
        perm2.append(s[index])
        ss(index + 1, perm2)


ss(1, [s[0]])
all_sum = 0
for way in all_s:
    tmp = 0
    for n in way:
        tmp += int(n)
    all_sum += tmp
print(all_sum)
