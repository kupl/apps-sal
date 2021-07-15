a = int(input())
studsx = list(map(int, input().split(' ')))
studs = [(studsx[x], x + 1) for x in range(a)]
i = [x for x in studs if x[0] == 1]
j = [y for y in studs if y[0] == 2]
k = [z for z in studs if z[0] == 3]
pairs = min(len(i), len(j), len(k))
print(pairs)
for l in range(pairs):
    print(str(i[l][1]) + ' ' + str(j[l][1]) + ' ' + str(k[l][1]))

